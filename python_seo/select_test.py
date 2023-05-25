from database import session
from table import Holiday

holidaylist = session.query(Holiday.holi_date).filter_by(
    holi_text="憲法記念日").all()

print(holidaylist)