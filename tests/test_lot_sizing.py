from datetime import date
from src.models.item import Item
from src.mrp.lot_sizing import apply_lot_sizing
D=date(2026,11,20)
def it(rule,q=0,moq=0,mul=1,poq=0): return Item('X','X','MAKE',1,rule,q,poq,moq,mul,0,0,'EA',1)
def test_lfl(): assert apply_lot_sizing(it('LFL'),{D:137})[D]==137
def test_foq(): assert apply_lot_sizing(it('FOQ',500),{D:501})[D]==1000
def test_moq_multiple(): assert apply_lot_sizing(it('LFL',0,50,10),{D:43})[D]==50
def test_poq(): assert apply_lot_sizing(it('POQ',0,0,1,2),{D:10,date(2026,11,25):20})[D]==30
