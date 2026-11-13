from datetime import date
from src.models.order import PlannedOrder
from src.models.routing import RoutingOperation,WorkCentre
from src.scheduling.backward_scheduler import schedule_operation_backward
def test_backward():
 p=PlannedOrder('P','FG',100,date(2026,11,17),date(2026,11,20),'MRP'); op=RoutingOperation('FG',10,'WC',30,5); wc=WorkCentre('WC','WC',960); s,e=schedule_operation_backward(p,op,wc,{},date(2026,11,14)); assert e is None and s.start_date==date(2026,11,20) and s.total_minutes==530
def test_capacity_short():
 p=PlannedOrder('P','FG',100,date(2026,11,17),date(2026,11,20),'MRP'); op=RoutingOperation('FG',10,'WC',30,5); wc=WorkCentre('WC','WC',960); used={d:960 for d in [date(2026,11,20),date(2026,11,19),date(2026,11,18),date(2026,11,17),date(2026,11,16),date(2026,11,14)]}; s,e=schedule_operation_backward(p,op,wc,used,date(2026,11,14)); assert s is None and e=='CAPACITY_SHORT'
