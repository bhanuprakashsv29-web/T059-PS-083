from datetime import timedelta
def is_working_day(d,holidays): return d.weekday()!=6 and d not in holidays
def subtract_working_days(start_date,working_days,holidays):
    d=start_date
    while working_days>0:
        d-=timedelta(days=1)
        if is_working_day(d,holidays): working_days-=1
    return d
def calculate_release_date(need_date,lead_time_days,today,holidays):
    r=subtract_working_days(need_date,lead_time_days,holidays)
    return (today,'PAST_DUE') if r<today else (r,None)
