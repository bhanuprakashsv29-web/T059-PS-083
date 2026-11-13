from dataclasses import dataclass
@dataclass
class RoutingOperation:
    item_id:str; operation_no:int; work_centre_id:str; setup_minutes:float; run_minutes_per_unit:float
@dataclass
class WorkCentre:
    work_centre_id:str; description:str; daily_capacity_minutes:float=960
