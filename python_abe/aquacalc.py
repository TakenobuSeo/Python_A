import datetime
from datetime import date
import sys
args = sys.argv
date_today = args[1]
adult_num = int(args[2])
ch_num = int(args[3])
year = int(date_today[:4])
month = int(date_today[4:6])
day = int(date_today[6:])
dt = date(year,month,day)
week_day = dt.strftime("%a")
if week_day == "Sat" or week_day == "Sun":
    sum = adult_num * 2400 + ch_num * 1500
else:
    sum = adult_num * 2000 + ch_num * 1200
print(sum, end ="")
