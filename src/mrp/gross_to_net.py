from collections import defaultdict
from src.models.order import MRPPeriod
def calculate_gross_requirements(mps_orders):
    out=defaultdict(lambda:defaultdict(float))
    for o in mps_orders: out[o.item_id][o.due_date]+=o.quantity
    return out
def calculate_scheduled_receipts(open_orders):
    out=defaultdict(lambda:defaultdict(float))
    for o in open_orders:
        if o.status.upper()=='OPEN': out[o.item_id][o.due_date]+=o.quantity
    return out
def calculate_mrp_for_item(item_id,periods,on_hand,safety_stock,gross_requirements,scheduled_receipts):
    rows=[]; prev=on_hand
    for p in periods:
        gr=gross_requirements.get(p,0.0); sr=scheduled_receipts.get(p,0.0); before=prev+sr-gr; net=max(0.0,safety_stock-before); rec=net; avail=before+rec
        rows.append(MRPPeriod(item_id,p,gr,sr,avail,net,rec,0.0)); prev=avail
    return rows
