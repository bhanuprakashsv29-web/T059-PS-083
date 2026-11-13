from datetime import date
from src.models.item import Item
from src.models.bom import BOMLine
from src.mrp.explosion import explode_bom,calculate_component_requirement

def test_scrap_rounding():
    i={'C':Item('C','C','MAKE',1,'LFL',0,0,0,1,0,5,'EA',1)}; b=[BOMLine('P','C',3,date(2026,1,1),None)]
    assert explode_bom('P',100,date(2026,11,20),b,i)['C']==316

def test_effectivity_switch():
    i={'C1':Item('C1','C1','MAKE',1,'LFL',0,0,0,1,0,0,'EA',1),'C2':Item('C2','C2','MAKE',1,'LFL',0,0,0,1,0,0,'EA',1)}
    b=[BOMLine('P','C1',1,date(2026,1,1),date(2026,6,30)),BOMLine('P','C2',1,date(2026,7,1),None)]
    assert explode_bom('P',10,date(2026,6,1),b,i)=={'C1':10}
    assert explode_bom('P',10,date(2026,8,1),b,i)=={'C2':10}
