from database import session
from sqlalchemy.sql import func, desc
from tables import MstMerchadise, TblStock, TblMoney, TblMessage
from datetime import datetime


def get_items_dict() -> dict:
    '''在庫がある商品の商品名と価格を辞書型で返す'''
    item_records = session.query(MstMerchadise.name, MstMerchadise.price).join(TblStock, TblStock.id == MstMerchadise.id).filter(TblStock.stock > 0).all()
    item_dict = { name:price for name, price in item_records}
    return item_dict

def print_items(items: dict) -> None:
    '''商品名と価格の一覧を出力する'''
    for key in  items.keys():
        print(f"{key}:{items[key]}円")

def renew_available_items() -> dict:
    '''在庫がある商品名と価格を全て出力し、{商品名: 価格}の辞書型で返す'''
    items_available = get_items_dict()
    print_items(items_available)
    return items_available

def store_change(money: int) -> None:
    '''投入金を格納する'''
    CHANGE_RECORDS = session.query(TblMoney).order_by(desc(TblMoney.price)).all()

    for record in CHANGE_RECORDS:
        change_number = money // record.price

        # その種類のお釣りがある場合
        if change_number > 0:
            record.number += change_number
            money %= record.price
            session.add(record)
    
    session.commit()

def pay_out_change(money: int) -> None:
    '''おつりを払い出す'''
    def get_change_unit_name(num: int) -> bool:
        '''単位が札か玉かを返す'''
        if num >= 1000:
            return "札"
        else:
            return "玉"
    
    # おつりの内容を出力
    print("おつり")
    CHANGE_RECORDS = session.query(TblMoney).order_by(desc(TblMoney.price)).all()
    SEQ = session.query(TblMessage).count() + 1
    for record in CHANGE_RECORDS:
        change_number = money // record.price

        # その種類のお釣りがある場合
        if change_number > 0:
            record.number -= change_number
            money %= record.price
            session.add(record)
            print(f"{record.price}円{get_change_unit_name(record.price)}:{change_number}枚")

            # 釣銭が残り少ないことをtbl_messageに通知
            if record.number <= 10:
                message = TblMessage(
                    seq = SEQ,
                    message = f"{record.price}円の残枚数が{record.number}枚になりました。確認してください",
                    datetime = datetime.now(),
                )
                session.add(message)
                SEQ += 1
                
    session.commit()

def get_lowest_price() -> int:
    '''在庫がある中で一番安い商品の価格を返す'''
    result = session.query(func.min(MstMerchadise.price)).join(TblStock, TblStock.id == MstMerchadise.id).filter(TblStock.stock > 0).one()
    return result[0]

def buy_item(buy_item_name: str) -> None:
    '''与えられた商品名の商品の在庫を1減らす'''
    target_record = session.query(TblStock).join(MstMerchadise, MstMerchadise.id == TblStock.id).filter(MstMerchadise.name == buy_item_name).one()
    target_record.stock -= 1
    session.add(target_record)
    session.commit()
