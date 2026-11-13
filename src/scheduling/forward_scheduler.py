from datetime import timedelta
from src.models.schedule import ScheduledOperation
from src.scheduling.capacity import calculate_operation_minutes

def is_working_day(d): return d.weekday()!=6
def next_working_day(d):
    d+=timedelta(days=1)
    while not is_working_day(d): d+=timedelta(days=1)
    return d

def schedule_operation_forward(planned_order,operation,work_centre,used_capacity,start_date):
    remaining=calculate_operation_minutes(operation,planned_order.quantity); start=None; end=None; d=start_date
    while remaining>0:
        if not is_working_day(d): d=next_working_day(d); continue
        used=used_capacity.get(d,0.0); available=max(0.0,work_centre.daily_capacity_minutes-used)
        if available>0:
            take=min(remaining,available); used_capacity[d]=used+take; remaining-=take
            if start is None: start=d
            end=d
        if remaining<=0: break
        d=next_working_day(d)
    return ScheduledOperation(planned_order.order_id,planned_order.item_id,operation.operation_no,operation.work_centre_id,planned_order.quantity,start,end,operation.setup_minutes,operation.run_minutes_per_unit*planned_order.quantity,calculate_operation_minutes(operation,planned_order.quantity))
