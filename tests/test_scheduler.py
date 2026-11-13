from datetime import date
from src.models.order import PlannedOrder
from src.models.routing import RoutingOperation,WorkCentre
from src.scheduling.scheduler import schedule_planned_order
def test_scheduler():
 p=PlannedOrder('P','FG',100,date(2026,11,17),date(2026,11,20),'MRP'); ops=[RoutingOperation('FG',10,'W1',30,5),RoutingOperation('FG',20,'W2',20,3)]; w={'W1':WorkCentre('W1','W1',960),'W2':WorkCentre('W2','W2',960)}; s,e=schedule_planned_order(p,ops,w,{},date(2026,11,14)); assert len(s)==2 and not e and [x.operation_no for x in s]==[10,20]
