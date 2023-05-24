import sys
from datetime import date
from datetime import datetime
from database import session
from tables import Holiday

def is_holiday(date: date) -> bool:
    '''その日付が祝日か返す'''
    selected = session.query(Holiday.holi_date).filter_by(holi_date=date).all()
    if len(selected) > 0:
        return True
    else:
        return False


args = sys.argv
dt = datetime.strptime(args[1], "%Y%m%d")
count_adult = int(args[2])
count_child = int(args[3])

# 土日と平日で値段を変える
if dt.strftime("%a") in ["Sat", "Sun"] or is_holiday(dt):
    PRICE_ADULT = 2400
    PRICE_CHILD = 1500
else:
    PRICE_ADULT = 2000
    PRICE_CHILD = 1200

total_price = PRICE_ADULT * count_adult + PRICE_CHILD * count_child

print(total_price, end="")
