import sys
from datetime import date
from datetime import datetime
from database import session
from attend_num import AttendNum

def get_seq_number(date: date) -> int:
    '''その日付の既存レコード件数+1を返す'''
    selected_num = session.query(AttendNum.entry_date).filter_by(entry_date=date).count()
    return selected_num + 1

args = sys.argv
ENTRY_DATE = datetime.strptime(args[1], "%Y%m%d")
COUNT_ADULT = int(args[2])
COUNT_CHILD = int(args[3])
SEQ_NUM = get_seq_number(ENTRY_DATE)

attend_num = AttendNum(
    entry_date = ENTRY_DATE,
    seq = SEQ_NUM,
    adult = COUNT_ADULT,
    child = COUNT_CHILD
)

print(attend_num)

session.add(attend_num)
session.commit()

