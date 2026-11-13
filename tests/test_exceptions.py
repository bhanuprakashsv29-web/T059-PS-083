from datetime import date
from src.exceptions.exception_engine import create_past_due_exception,create_expedite_exception,create_deexpedite_exception,create_cancel_exception,create_capacity_short_exception
def test_exception_types():
 d=date(2026,11,20); xs=[create_past_due_exception('C','O',d),create_expedite_exception('C','O',d),create_deexpedite_exception('C','O',d),create_cancel_exception('C','O',d),create_capacity_short_exception('C','O',d)]
 assert [x.exception_type for x in xs]==['PAST_DUE','EXPEDITE','DEEXPEDITE','CANCEL','CAPACITY_SHORT']
