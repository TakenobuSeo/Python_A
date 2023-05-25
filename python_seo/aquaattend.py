from datetime import date
#import datetime
from datetime import date
from database import session
from table import Attendnum

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

#print(session.query(Attendnum.date).all())
print(dt)
dt_test = session.query(Attendnum).filter_by(entry_date=dt).count() + 1
print(dt_test)
 # 同じ日付がいくつあるか

#print(dt_test)
aquaattend = Attendnum(
    entry_date = dt,
    seq = dt_test,
    adult = ad_num,
    child = ch_num
)

session.add(aquaattend)

session.commit()
