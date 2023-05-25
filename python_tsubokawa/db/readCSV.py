import csv
from datetime import date

with open('holiday.csv', 'r',encoding = "utf-8-sig") as f:
    reader = csv.reader(f)
    for line in reader:
        complicated_day = line[0]
        # print(int(line[0]))
        year = int(complicated_day[:4])
        # print(type(year))
        month = int(complicated_day[4:6])
        # print(f'year : {year}')
        # print(f'month : {month}')
        day = int(complicated_day[6:])
        # print(f'day:{day}')
        holiday_date = date(year,month,day)
        print(f'holiday_date:{holiday_date}')

        # print(complicated_day)
        print(f'日の名前:{line[1]}')

