from dataclasses import dataclass
from datetime import date
@dataclass
class MRPException:
    exception_type:str; item_id:str; message:str; order_id:str|None=None; due_date:date|None=None
def _make(t,item_id,order_id,due_date,msg): return MRPException(t,item_id,msg,order_id,due_date)
def create_past_due_exception(item_id,order_id,due_date): return _make('PAST_DUE',item_id,order_id,due_date,f'Order {order_id} for {item_id} is past due.')
def create_expedite_exception(item_id,order_id,due_date): return _make('EXPEDITE',item_id,order_id,due_date,f'Order {order_id} for {item_id} should be expedited.')
def create_deexpedite_exception(item_id,order_id,due_date): return _make('DEEXPEDITE',item_id,order_id,due_date,f'Order {order_id} for {item_id} can be de-expedited.')
def create_cancel_exception(item_id,order_id,due_date): return _make('CANCEL',item_id,order_id,due_date,f'Order {order_id} for {item_id} should be cancelled.')
def create_capacity_short_exception(item_id,order_id,due_date): return _make('CAPACITY_SHORT',item_id,order_id,due_date,f'Insufficient capacity for {order_id} of {item_id}.')
