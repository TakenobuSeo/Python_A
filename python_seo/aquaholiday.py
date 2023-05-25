from datetime import date
#import datetime
from datetime import date
from database import session
from table import Holiday

import sys

args = sys.argv

day = args[1]
ad_num = int(args[2])
ch_num = int(args[3])

y = int(day[:4])
m = int(day[4:6])
d = int(day[6:])

#print(y,m,d)
dt = date(y, m, d)
#dt = datetime.date(2022, 6, 4)

#print(dt)
youbi = dt.strftime("%a")

#print(youbi)

if youbi == "Sun" or youbi == "Sat":
    sum = (2400 * ad_num) + (1500 * ch_num)
    print(sum)

elif session.query(Holiday.holi_text).filter_by(holi_date=dt):
    sum = (2400 * ad_num) + (1500 * ch_num)
    print(sum)

else:
    sum = (2000 * ad_num) + (1200 * ch_num)
    print(sum)
