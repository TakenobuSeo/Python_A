from datetime import date
from database import session
from table import Holiday

holiday = session.query(Holiday).filter_by(holi_date=date(2024,1,1)).first()

holiday.holi_date = "2023-1-2"
holiday.holi_text = "お正月"

session.add(holiday)

session.commit()