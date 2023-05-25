from database import session
from tables import Holiday
from datetime import date
# holidaylist = session.query(Holiday).all()

# holiday = Holiday(
#     holi_date = date(2023,1,9),
#     holi_text = '成人の日'
# )



# print(len(holiday_data))
# print(holiday_data.keys())
    # print(key)
holiday = Holiday(
        holi_date = date(2024,1,1),
        holi_text = 'お正月'
    )
session.add(holiday)


session.commit()