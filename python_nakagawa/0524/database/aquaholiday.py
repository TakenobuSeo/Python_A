import sys
args = sys.argv
from datetime import datetime
from datetime import date
from database import session
from tables import Holiday

date = args[1]
adultNum = int(args[2])
childNum = int(args[3])
holidayList = session.query(Holiday.holi_date).all()

dt = datetime.strptime(date, "%Y%m%d")
day = dt.date()
week = dt.strftime("%a") # 日付を曜日に変換

#祝日かどうか
holiday = False
for i in holidayList:
  if day == i[0]:
     holiday = True
     
# 土、日、祝は大人2400円、子供1500円
if week == "Sat" or week == "Sun" or holiday == True:
    adultPrice  = 2400
    childPrice = 1500
else : 
  adultPrice = 2000
  childPrice = 1200

sum = adultPrice * adultNum + childPrice * childNum
print(f'合計金額は{sum}円', end="")