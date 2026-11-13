from datetime import date
from src.models.order import PlannedOrder
from src.models.routing import RoutingOperation,WorkCentre
from src.scheduling.forward_scheduler import schedule_operation_forward
def test_forward():
 p=PlannedOrder('P','FG',100,date(2026,11,17),date(2026,11,20),'MRP'); op=RoutingOperation('FG',10,'WC',30,5); wc=WorkCentre('WC','WC',960); s=schedule_operation_forward(p,op,wc,{date(2026,11,14):960},date(2026,11,14)); assert s.start_date==date(2026,11,16)
