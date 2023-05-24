from database import session
from tables import Holiday
import csv
from datetime import date

#holiday.csvを読み込む
filename = '/home/matcha-23training/Python_A/python_nakagawa/0524/database/data/holiday.csv'
with open(filename, encoding='utf-8_sig', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        date_today = str(row[0])
        year = int(date_today[:4])
        month = int(date_today[4:6])
        day = int(date_today[6:])
        # holiday = Holiday(
        #     holi_date = date(year,month,day),
        #     holi_text = row[1]
        # )
        # session.add(holiday)
        # session.commit()