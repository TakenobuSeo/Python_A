from database import session
from tables import Holiday

holidaylist = session.query(Holiday).all()
holidaylist = session.query(Holiday.holi_date).filter_by(holi_text="憲法記念日").all()