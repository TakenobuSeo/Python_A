import datetime
import database
from datetime import date
from database import session
from vend_table import Money, Stock, Merchandise, Message
from sqlalchemy import select

def show_stock():
    '''Stockデータの取得し在庫があるものを表示'''
    stocks_datas = session.query(Merchandise.name, Merchandise.price,Stock.stock).join(Merchandise, Merchandise.id == Stock.id)
    # print(stocks_datas)
    for stock in stocks_datas:
        # 在庫があるものだけ表示
        if stock.stock >0:
            print(f'{stock.name}:{stock.price}')


def show_money(money_stock):
    '''
    Moneyデータのnumを取得する関数
    '''
    
    money_datas = session.query(Money.price, Money.number).all()
    for money_data in money_datas:
        # お金の在庫を辞書型で取得

        # お金の在庫が10枚以下の時に足りないお金(10000札以外)を取得してくる
        if money_data.number <= 10 and money_data.price != 10000:
            money_stock[money_data.price] = money_data.number
    
    return money_stock

money_stock = {}     

print(show_money(money_stock))


def test(update_name):
    update_id = session.query(Merchandise.id, Stock).join(
        Merchandise, Merchandise.id == Stock.id).filter_by(
            name = update_name
        ).first()
    print(update_id.id)

# test('コーヒー')
# show_stock()


def update_money(update_price, update_number):
    '''Moneyの更新処理'''
    # 更新対象のお金の枚数を取得
    money = session.query(Money).filter_by(
        # update_price : 更新対象のお金
        price = update_price
    ).first()

    #枚数の更新
    # print(f'type_money_num{type(money.number)}')
    # print(f'type_update:{type(update_number)}')
    money.number += update_number
    session.add(money)
    session.commit()

# update_money(5000,1)
# update_money(10000,10)


def update_stock(update_name, update_stock=-1):
    '''
    Stockの更新処理
    第一引数に処理する商品名、第2引数に処理する個数（デフォルト:-1）
    
    '''
    # 商品名から商品idを取得する処理
    update_id = session.query(Merchandise.id, Stock).join(
        Merchandise, Merchandise.id == Stock.id).filter_by(
            name = update_name
        ).first()
    # 更新するidはupdate_id.idに保存


    stock = session.query(Stock).filter_by(
        #更新するidとidが一致する在庫のデータを取得
        id = update_id.id
    ).first()

    #↓増分を記入
    stock.stock += update_stock
    session.add(stock)
    session.commit()


# update_stock('コーヒー', 10)


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