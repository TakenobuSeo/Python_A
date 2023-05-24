from database import session
from tables import Holiday
from datetime import date

holidaydate = session.query(Holiday.holi_text).filter_by(
    holi_date=date(2023,1,1)).first()
print("------------------------------")
if holidaydate == None:
    print('平日です')
else:
    print(holidaydate)
# print(holidaylist)
# for holidaydate in holidaydates:
#     print(holidaydate)

# holiday = session.query(Holiday.holi_date).fil