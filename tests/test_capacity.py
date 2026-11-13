from src.models.routing import RoutingOperation,WorkCentre
from src.scheduling.capacity import calculate_operation_minutes,is_within_capacity
def test_minutes():
 op=RoutingOperation('FG001',10,'WC01',30,5); assert calculate_operation_minutes(op,100)==530
def test_capacity():
 wc=WorkCentre('WC01','WC01',960); assert is_within_capacity(960,wc) and not is_within_capacity(961,wc)
