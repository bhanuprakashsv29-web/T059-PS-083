from datetime import date
from src.models.order import PlannedOrder,MPSOrder
from src.mrp.pegging import create_pegging
def test_pegging():
 p=PlannedOrder('PLN-C', 'C',300,date(2026,11,15),date(2026,11,20),'MRP'); m=MPSOrder('MPS001','FG001',100,date(2026,11,20)); x=create_pegging(p,m)
 assert x['mps_order_id']=='MPS001' and x['top_level_item']=='FG001' and x['planned_quantity']==300
