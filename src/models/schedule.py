from dataclasses import dataclass
from datetime import date
@dataclass
class ScheduledOperation:
    planned_order_id:str; item_id:str; operation_no:int; work_centre_id:str; quantity:float; start_date:date; end_date:date; setup_minutes:float; run_minutes:float; total_minutes:float
