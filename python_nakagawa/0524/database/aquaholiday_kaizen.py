from datetime import datetime
from database import session
from datetime import date
from tables import Holiday
import sys
args = sys.argv

input_day = args[1]
adult_num = int(args[2])  # 大人の人数
child_num = int(args[3])  # 子供の人数

# 祝日のデータを取得
holiday_list = session.query(Holiday.holi_date).all()

dt = datetime.strptime(input_day, "%Y%m%d")
date = dt.date()
week = dt.strftime("%a")  # 日付を曜日に変換

# 休日かどうかを判定
is_holiday = False
for holi in holiday_list:
    if any([week == "Sat", week == "Sun", date == holi[0]]):
        is_holiday = True

# 土、日、祝は大人2400円、子供1500円
adult_price = 2400 if is_holiday else 2000
child_price = 1500 if is_holiday else 1200

adult_price_sum = adult_price * adult_num
child_price_sum = child_price * child_num

sum = adult_price_sum + child_price_sum  # 合計金額
print(f'合計金額は{sum}円', end="")
