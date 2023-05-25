import datetime
import database
from datetime import date
from database import session
from vend_table import Money, Stock, Merchandise, Message
from sqlalchemy import select

def show_stock():
    '''Stockデータの取得し在庫があるものを表示'''
    stocks_datas = session.query(Merchandise.name, Merchandise.price,Stock.stock).join(Merchandise, Merchandise.id == Stock.id)
    for stock in stocks_datas:
        # 在庫があるものだけ表示
        if stock.stock >0:
            print(f'{stock.name}:{stock.price}')




# show_stock()


def update_money(update_price, update_number):
    '''Moneyの更新処理'''
    # 更新対象のお金の枚数を取得
    money = session.query(Money).filter_by(
        # update_price : 更新対象のお金
        price = update_price
    ).first()

    #枚数の更新
    money.number += update_number
    session.add(money)
    session.commit()



def update_stock(update_id, update_stock):
    '''Stockの更新処理'''
    stock = session.query(Stock).filter_by(
        # ↓条件記入
        id = update_id
    ).first()

    #↓増分を記入
    stock.stock += update_stock
    session.add(stock)
    session.commit()



def insert_message(price, number):
    '''Messageの追加処理'''
    #Messageテーブルのデータ数を取得
    msg_num = session.query(Message.seq).count()
    #連番付与
    seq = msg_num + 1
    message_text = f'{price}の残枚数が{number}枚になりました。確認してください。' 
    message = Message(
        seq = seq,
        message = message_text,
        datetime = datetime.datetime.now()
    )
    session.add(message)
    session.commit()





# insert_message(100, 50)

# session.commit()