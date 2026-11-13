from datetime import date
from src.models.item import Item
from src.models.order import PlannedOrder
from src.scheduling.priority import sort_planned_orders
def item(i,c): return Item(i,i,'MAKE',1,'LFL',0,0,0,1,0,0,'EA',c)
def order(i,it,q,d): return PlannedOrder(i,it,q,date(2026,11,14),d,'MRP')
def test_priority():
 items={'A':item('A',1000),'B':item('B',400)}; a=order('O2','A',10,date(2026,11,20)); b=order('O1','B',10,date(2026,11,20)); assert [x.order_id for x in sort_planned_orders([a,b],items)]==['O2','O1']
def test_edd():
 items={'A':item('A',1000)}; a=order('O2','A',10,date(2026,11,21)); b=order('O1','A',10,date(2026,11,20)); assert sort_planned_orders([a,b],items)[0].order_id=='O1'
