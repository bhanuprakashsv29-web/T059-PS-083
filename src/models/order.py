from dataclasses import dataclass
from datetime import date
from typing import Optional
@dataclass
class MPSOrder:
    order_id:str; item_id:str; quantity:float; due_date:date
@dataclass
class InventoryRecord:
    item_id:str; on_hand:float
@dataclass
class OpenOrder:
    order_id:str; item_id:str; order_type:str; quantity:float; due_date:date; status:str='OPEN'
@dataclass
class PlannedOrder:
    order_id:str; item_id:str; quantity:float; release_date:date; due_date:date; source:str; pegging:Optional[dict]=None
@dataclass
class MRPPeriod:
    item_id:str; period:date; gross_requirement:float; scheduled_receipt:float; projected_available:float; net_requirement:float; planned_order_receipt:float; planned_order_release:float
