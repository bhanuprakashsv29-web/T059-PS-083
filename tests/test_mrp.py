from datetime import date
from src.mrp.gross_to_net import calculate_mrp_for_item

def test_mrp_safety_stock():
    rows=calculate_mrp_for_item('FG', [date(2026,11,20)],20,10,{date(2026,11,20):100},{})
    assert rows[0].net_requirement==90 and rows[0].projected_available==10
