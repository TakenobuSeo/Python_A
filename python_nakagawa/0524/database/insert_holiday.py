from datetime import date
from database import session
from tables import Holiday

holiday = Holiday(
    holi_date = date(2023, 1, 9),
    holi_text = "成人の日",
)

session.add(holiday)
session.commit()