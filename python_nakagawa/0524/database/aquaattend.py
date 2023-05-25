import sys
args = sys.argv
from datetime import datetime
from datetime import date
from database import session
from tables import AttendnumKey

date = args[1]
adultNum = int(args[2])
childNum = int(args[3])

dt = datetime.strptime(date, "%Y%m%d")
day = dt.date()
print(day)

# 日付が同じデータを取得
entryDateNum = session.query(AttendnumKey).filter(AttendnumKey.entry_date==day).count()
print(entryDateNum)

data = AttendnumKey(
    entry_date = day,
    seq = int(entryDateNum) +1,
    adult = adultNum,
    child = childNum
)

session.add(data)
session.commit()