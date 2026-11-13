from datetime import date
from src.mrp.lead_time import subtract_working_days,calculate_release_date
D=date(2026,11,23)
def test_working_days(): assert subtract_working_days(D,1,set())==date(2026,11,21)
def test_holiday(): assert subtract_working_days(D,2,{date(2026,11,20)})==date(2026,11,19)
def test_past_due(): assert calculate_release_date(date(2026,11,15),5,date(2026,11,14),set())[1]=='PAST_DUE'
