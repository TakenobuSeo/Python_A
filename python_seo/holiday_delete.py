from datetime import date
from database import session
from table import Holiday

result = session.query(Holiday).filter_by(holi_date=date(2023,1,2)).delete()

session.commit()