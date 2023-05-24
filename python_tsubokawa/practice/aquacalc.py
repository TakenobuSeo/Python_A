#モジュールをインポート
from datetime import date
import sys





args = sys.argv
input_date = args[1]
adult_num = int(args[2])
child_num = int(args[3])

#第２引数から年月日を抽出
year = int(input_date[0:4])

month = int(input_date[4:6])

day = int(input_date[6:])



input_dates = date(year,month,day)
#曜日算出
#0:Mon, 1:Tue, ...
calc_weekday = input_dates.weekday()

#以下でもOK　出力はMon, Tue, になる
# calc_weekday = input_dates.strftime("%a")
print(calc_weekday)


#子どもと大人の金額データ
price_data_adult = [2000, 2400]
price_data_child = [1200, 1500]

# print(calc_weekday)
if calc_weekday == 5 or calc_weekday == 6:
#土日の金額処理
    price_adult = price_data_adult[1]
    price_child = price_data_child[1]
else:
    #平日の金額処理
    price_adult = price_data_adult[0]
    price_child = price_data_child[0]

price_total = price_adult * adult_num +price_child * child_num
print(price_total, end="")


