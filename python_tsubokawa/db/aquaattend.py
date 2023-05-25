from database import session
from aquaattend_table import Attend
from datetime import date
import sys

#入力値の取得
args = sys.argv
complicated_date = args[1]
adult_num = int(args[2])
child_num = int(args[3])

#日付を分割
year = int(complicated_date[0:4])
month = int(complicated_date[4:6])

day = int(complicated_date[6:])
output_date = date(year,month,day)

# print(output_date)
#連番値の設定
seq_num = session.query(Attend.seq).filter_by(
    entry_date=output_date).count()
seq_num += 1 #連番付与


attend = Attend(
    entry_date = output_date,
    seq = seq_num,
    adult =adult_num,
    child = child_num
)

# print(len(holiday_data))
# print(holiday_data.keys())
    # print(key)

session.add(attend)


session.commit()