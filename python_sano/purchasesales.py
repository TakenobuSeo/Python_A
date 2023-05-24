import sys
from datetime import date
from datetime import datetime
from database import session
from prchasesales_tables import MstHinmoku, TblZaiko


def registration_item(args) -> None:
    '''品目データを登録する'''
    ID = args[2]
    NAME = args[3]

    item = len(session.query(MstHinmoku).filter_by(id=ID).all())
    if item > 0:
        print(f"品目マスタに{ID}は登録済みです")
        return
    
    hinmoku = MstHinmoku(
        id = ID,
        name = NAME
    )

    session.add(hinmoku)
    session.commit()
    print(f"品目マスタに{ID}, {NAME}を登録しました")


def process_arrival(args) -> None:
    '''仕入れデータを登録する'''
    ID = args[2]
    UNIT = args[3]
    UNIT_PRICE = int(args[4])
    ARRIVALSTOCK = int(args[5])

    CURRENT_STOCK = session.query(TblZaiko.stock).filter_by(id=ID).first()[0]
    if not CURRENT_STOCK:
        CURRENT_STOCK = 0

    zaiko = TblZaiko(
        id = ID,
        unit = UNIT,
        unitprice = UNIT_PRICE,
        stock = CURRENT_STOCK + ARRIVALSTOCK
    )

    session.add(zaiko)
    session.commit()
    print(f"品目{ID}（単価：{UNIT_PRICE}円）を{ARRIVALSTOCK}{UNIT}仕入れました")

def process_sales(args):
    '''売上データを登録する'''

    ID = args[2]
    UNIT = args[3]
    UNIT_PRICE = int(args[4])
    SALED_STOCK = int(args[5])

    zaiko = session.query(TblZaiko).filter_by(id=ID, unit=UNIT, unitprice = UNIT_PRICE).first()
    CURRENT_STOCK = zaiko.stock
    
    if not CURRENT_STOCK:
        CURRENT_STOCK = 0

    if SALED_STOCK > CURRENT_STOCK:
        print("売上数量に対して在庫が足りません。在庫を確認してください")
        return

    zaiko.stock = CURRENT_STOCK - SALED_STOCK

    session.add(zaiko)
    session.commit()
    print(f"品目{ID}（単価：{UNIT_PRICE}円）を{SALED_STOCK}{UNIT}売上げました")

def print_all_zaiko():
    zaiko = session.query(TblZaiko.id, MstHinmoku.name, TblZaiko.stock, TblZaiko.unit, TblZaiko.unitprice).join(MstHinmoku, MstHinmoku.id == TblZaiko.id).all()
    for item in zaiko:
        print(f"品目{item.id}（{item.name}）の在庫：{item.stock}{item.unit}（単価：{item.unitprice}円）")

def main(args):
    """
    メイン関数
    """
    args = sys.argv
    mode = args[1]

    if mode == "1":
        return registration_item(args)
    elif mode == "2":
        return process_arrival(args)
    elif mode == "3":
        return process_sales(args)
    elif mode == "4":
        return print_all_zaiko()


if __name__ == "__main__":
    main(sys.argv)

