from src.scheduling.backward_scheduler import schedule_operation_backward
from src.scheduling.forward_scheduler import schedule_operation_forward
def schedule_planned_order(planned_order,operations,work_centres,used_capacity,today):
    schedules=[]; exceptions=[]
    for op in sorted(operations,key=lambda x:x.operation_no,reverse=True):
        wc=work_centres[op.work_centre_id]
        s,e=schedule_operation_backward(planned_order,op,wc,used_capacity,today)
        if s: schedules.append(s); continue
        schedules.append(schedule_operation_forward(planned_order,op,wc,used_capacity,today)); exceptions.append('CAPACITY_SHORT')
    schedules.sort(key=lambda x:x.operation_no); return schedules,exceptions
