from datetime import date
import pytest
from src.mrp.low_level_code import calculate_low_level_codes
from src.models.item import Item
from src.models.bom import BOMLine

def item(i): return Item(i,i,'MAKE',1,'LFL',0,0,0,1,0,0,'EA',1)
def test_low_level_codes():
    items={i:item(i) for i in ['A','B','C','D']}; bom=[BOMLine('A','B',1,date(2026,1,1),None),BOMLine('B','C',1,date(2026,1,1),None),BOMLine('C','D',1,date(2026,1,1),None)]
    assert calculate_low_level_codes(items,bom)=={'A':0,'B':1,'C':2,'D':3}
def test_cycle():
    items={i:item(i) for i in ['A','B']}; bom=[BOMLine('A','B',1,date(2026,1,1),None),BOMLine('B','A',1,date(2026,1,1),None)]
    with pytest.raises(ValueError): calculate_low_level_codes(items,bom)
