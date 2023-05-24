from database import session
from tables import Holiday
import csv
from datetime import date
holidaylist=session.query(Holiday).all()

print(holidaylist)
for holiday in holidaylist:
    print(holiday.holi_date,holiday.holi_text)