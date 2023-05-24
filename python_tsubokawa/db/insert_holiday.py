from database import session
from tables import Holiday
from datetime import date
# holidaylist = session.query(Holiday).all()

# holiday = Holiday(
#     holi_date = date(2023,1,9),
#     holi_text = '成人の日'
# )

holiday_data = {
    '成人の日' : date(2023,1,9),
    '建国記念日' : date(2023,2,11),
    '天皇誕生日' : date(2023,2,23),
    '春分の日' : date(2023,3,21),
    '昭和の日' : date(2023,4,29),
    '憲法記念日' : date(2023,5,3),
    'みどりの日' : date(2023,2,4),
    '子どもの日' : date(2023,5,5),
    '海の日' : date(2023,7,17),
    '山の日' : date(2023,8,11),
    '敬老の日' : date(2023,9,18),
    '秋分の日' : date(2023,9,23),
    'スポーツの日' : date(2023,10,9),
    '文化の日' : date(2023,11,3),
    '勤労感謝の日' : date(2023,11,23),
}

# print(len(holiday_data))
# print(holiday_data.keys())
for key in holiday_data.keys():
    # print(key)
    holiday = Holiday(
        holi_date = holiday_data[key],
        holi_text = key
    )

    session.add(holiday)


session.commit()