def print_schedule_report(schedules):
    print("\nSCHEDULE")
    print("-"*110)
    for s in schedules:
        print(f"{s.start_date} | {s.end_date} | {s.work_centre_id} | {s.item_id} op{s.operation_no} | {s.planned_order_id} | {s.total_minutes:g} min")
