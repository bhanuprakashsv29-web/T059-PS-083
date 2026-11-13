from datetime import date
from src.models.item import Item
from src.models.order import InventoryRecord
from src.mrp.planning import plan_item

def test_plan_item():
    item=Item('FG001','Finished Product','MAKE',3,'LFL',0,0,0,1,10,0,'EA',1000)
    orders=plan_item(item,[date(2026,11,20)],InventoryRecord('FG001',20),{date(2026,11,20):100},{},date(2026,11,14),set())
    assert len(orders)==1 and orders[0].quantity==90 and orders[0].release_date==date(2026,11,17)
