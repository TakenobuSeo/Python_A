from database import session
from vend_table import Money, Message, Stock, Merchandise
from datetime import date

'''
初期値としてStock, Moneyをinsertするプログラム
'''

#Stock初期値をinsert

init_stock_data = {
    '0000000000' : 10,
    '1111111111' : 50,
    '2222222222' : 5,
    '3333333333' : 3,
}

# for key in init_stock_data.keys():
#     stock = Stock(
#         id = key,
#         stock = init_stock_data[key]
#     )

#     session.add(stock)

# お金の初期値をinsert

# price (お金の種類) : number(自販機内のお金の数)
init_money_data = {
    10 : 100,
    50 : 100,
    100 : 100,
    500 :25, 
    1000 : 50,
    5000 : 10,
    10000 : 0
}

# for key in init_money_data.keys():
#     money = Money(
#         price = key,
#         number = init_money_data[key]
#     )

#     session.add(money)

money = Money(
    price = 2000,
    number = 50
)
session.add(money)

session.commit()