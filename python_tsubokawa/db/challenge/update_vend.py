from datetime import date
from database import session
from vend_table import Money, Stock, Merchandise, Message

def update_money(update_price, update_number):
# Moneyの更新処理
    money = session.query(Money).filter_by(
        # ↓条件記入
        price = update_price
    ).first()

    #↓増分を記入
    money.number += update_number
    session.add(money)
    session.commit()

def update_stock(update_id, update_stock):
# Stockの更新処理
    stock = session.query(Stock).filter_by(
        # ↓条件記入
        id = update_id
    ).first()

    #↓増分を記入
    stock.stock += update_stock
    session.add(stock)
    session.commit()

# Messageテーブルのデータ数を返す処理
def get_Message_num():
    msg_num = session.query(Message.seq).count()
    return msg_num


def insert_message(msg_num, price, number, ):
#Messageの追加処理
    #連番付与
    seq = msg_num + 1
    message_text = f'{price}の残枚数が{number}枚になりました。確認してください。' 
    message = Message(

    )


print(get_Message_num())

# session.commit()