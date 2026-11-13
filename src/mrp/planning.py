from src.mrp.gross_to_net import calculate_mrp_for_item
from src.mrp.lot_sizing import apply_lot_sizing
from src.mrp.lead_time import calculate_release_date
from src.models.order import PlannedOrder
def plan_item(item,periods,inventory,gross_requirements,scheduled_receipts,today,holidays):
    rows=calculate_mrp_for_item(item.item_id,periods,inventory.on_hand,item.safety_stock,gross_requirements,scheduled_receipts)
    nets={r.period:r.net_requirement for r in rows if r.net_requirement>0}; lots=apply_lot_sizing(item,nets); out=[]
    for period,q in lots.items():
        if q<=0: continue
        release,exc=calculate_release_date(period,item.lead_time_days,today,holidays)
        out.append(PlannedOrder(f"PLN-{item.item_id}-{period}",item.item_id,q,release,period,'MRP'))
    return out
