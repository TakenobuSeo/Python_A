import datetime
from datetime import date
from database import session
from aqa_tables import Attendnum
import sys
args = sys.argv
date_today = args[1]
adult_num = int(args[2])
ch_num = int(args[3])
year = int(date_today[:4])
month = int(date_today[4:6])
day = int(date_today[6:])
dt = date(year,month,day)
items = session.query(Attendnum).all()
print(items)
num = session.query(Attendnum).filter(Attendnum.entry_date == dt).count()
attend = Attendnum(
    entry_date = date(year,month,day),
    seq = num+1,
    adult = adult_num,
    child = ch_num
)
session.add(attend)
session.commit()