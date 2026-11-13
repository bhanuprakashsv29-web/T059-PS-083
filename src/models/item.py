from dataclasses import dataclass
@dataclass
class Item:
    item_id:str; description:str; make_buy:str; lead_time_days:int; lot_size_rule:str; lot_size_quantity:float; period_order_quantity:int; minimum_order_quantity:float; order_multiple:float; safety_stock:float; scrap_percent:float; uom:str; standard_cost:float
