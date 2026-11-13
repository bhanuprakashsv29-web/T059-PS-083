from datetime import date
from src.loaders.item_loader import load_items
from src.loaders.bom_loader import load_bom
from src.loaders.routing_loader import load_routings
from src.loaders.mps_loader import load_mps
from src.loaders.order_loader import load_inventory,load_open_orders
from src.mrp.low_level_code import calculate_low_level_codes
from src.mrp.gross_to_net import calculate_gross_requirements,calculate_scheduled_receipts,calculate_mrp_for_item
from src.mrp.planning import plan_item
from src.mrp.explosion import explode_bom
from src.mrp.pegging import create_pegging
from src.scheduling.priority import sort_planned_orders
from src.scheduling.scheduler import schedule_planned_order

class PlanningEngine:
    def __init__(self,data_dir,today=None,holidays=None):
        self.data_dir=data_dir; self.today=today or date.today(); self.holidays=holidays or set()
        self.items=load_items(data_dir/'items.csv'); self.bom=load_bom(data_dir/'bom.csv'); self.routings,self.work_centres=load_routings(data_dir/'routings.csv'); self.mps=load_mps(data_dir/'mps.csv'); self.inventory=load_inventory(data_dir/'inventory.csv'); self.open_orders=load_open_orders(data_dir/'open_orders.csv')
        self.low_level_codes=calculate_low_level_codes(self.items,self.bom)
    def run(self):
        gross=calculate_gross_requirements(self.mps); receipts=calculate_scheduled_receipts(self.open_orders)
        periods=sorted({o.due_date for o in self.mps}|{o.due_date for o in self.open_orders})
        planned=[]; mrp_rows=[]
        for item_id in sorted(self.items,key=lambda x:(self.low_level_codes[x],x)):
            if item_id not in gross: continue
            inv=self.inventory.get(item_id); onhand=inv.on_hand if inv else 0
            rows=calculate_mrp_for_item(item_id,periods,onhand,self.items[item_id].safety_stock,gross.get(item_id,{}),receipts.get(item_id,{})); mrp_rows.extend(rows)
            planned.extend(plan_item(self.items[item_id],periods,inv or type('I',(),{'on_hand':0})(),gross.get(item_id,{}),receipts.get(item_id,{}),self.today,self.holidays))
        # explode top-level MPS into component requirements and plan components
        component_demands={}
        for m in self.mps:
            component_demands.update({k:component_demands.get(k,0)+v for k,v in explode_bom(m.item_id,m.quantity,m.due_date,self.bom,self.items).items()})
        for item_id in sorted(component_demands,key=lambda x:(self.low_level_codes.get(x,99),x)):
            item=self.items[item_id]; inv=self.inventory.get(item_id) or type('I',(),{'on_hand':0})(); periods2=sorted({m.due_date for m in self.mps}); p=plan_item(item,periods2,inv,{d:(component_demands[item_id] if d==periods2[0] else 0) for d in periods2},receipts.get(item_id,{}),self.today,self.holidays); planned.extend(p)
        # deterministic de-duplication
        unique={o.order_id:o for o in planned}; planned=list(unique.values()); planned=sort_planned_orders(planned,self.items)
        pegged=[]
        for p in planned:
            matches=[m for m in self.mps if m.item_id==p.item_id]
            if matches: p.pegging=create_pegging(p,matches[0])
            else: p.pegging={'planned_order_id':p.order_id,'mps_order_id':self.mps[0].order_id if self.mps else None,'top_level_item':self.mps[0].item_id if self.mps else None,'planned_item':p.item_id,'planned_quantity':p.quantity}
            pegged.append(p)
        used={}; schedules=[]; exceptions=[]
        ops_by_item={}
        for op in self.routings: ops_by_item.setdefault(op.item_id,[]).append(op)
        for p in planned:
            if self.items[p.item_id].make_buy.upper()=='MAKE' and p.item_id in ops_by_item:
                s,e=schedule_planned_order(p,ops_by_item[p.item_id],self.work_centres,used,self.today); schedules.extend(s); exceptions.extend(e)
        return {'low_level_codes':self.low_level_codes,'mrp_rows':mrp_rows,'planned_orders':planned,'schedules':schedules,'exceptions':exceptions}

def compare_plans(old,new):
    a={o.order_id:o for o in old}; b={o.order_id:o for o in new}; return {'added':[b[k] for k in b.keys()-a.keys()],'removed':[a[k] for k in a.keys()-b.keys()],'changed':[ (a[k],b[k]) for k in a.keys()&b.keys() if a[k].quantity!=b[k].quantity or a[k].due_date!=b[k].due_date or a[k].release_date!=b[k].release_date]}
