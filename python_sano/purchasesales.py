import sys
from datetime import date
from datetime import datetime
from database import session
from prchasesales_tables import MstHinmoku, TblZaiko

class ID():
    id: str

    def __init__(self, id):
        self.id = id

class Hinmoku(ID):
    name:str

    def __init__(self, id: str, name: str):
        super().__init__(id)
        self.name = name

    def registration_item(self) -> None:
        '''品目データを登録する'''

        item = len(session.query(MstHinmoku).filter_by(id=self.id).all())
        if item > 0:
            print(f"品目マスタに{self.id}は登録済みです")
            return
        
        hinmoku = MstHinmoku(
            id = self.id,
            name = self.name
        )

        session.add(hinmoku)
        session.commit()
        print(f"品目マスタに{self.id}, {self.name}を登録しました")

class Transaction(ID):
    unit: str
    unit_price: int
    change_stock_num: int

    def __init__(self, id: str, unit: str, unit_price: int, change_stock: int):
        super().__init__(id)
        self.unit = unit
        self.unit_price = unit_price
        self.change_stock_num = change_stock

    def get_current_zaiko(self) -> TblZaiko:
        '''自身の商品IDの現在のデータを返す'''
        current_zaiko = session.query(TblZaiko).filter_by(id=self.id, unit=self.unit, unitprice=self.unit_price).first()
        return current_zaiko
        

    def process_arrival(self) -> None:
        '''仕入れデータを登録する'''

        zaiko = self.get_current_zaiko()
        if zaiko:
            zaiko.stock = zaiko.stock + self.change_stock_num
        else:
            zaiko = TblZaiko(
            id = self.id,
            unit = self.unit,
            unitprice = self.unit_price,
            stock = self.change_stock_num
        )

        session.add(zaiko)
        session.commit()
        print(f"品目{self.id}（単価：{self.unit_price}円）を{self.change_stock_num}{self.unit}仕入れました")

    def process_sales(self):
        '''売上データを登録する'''

        zaiko = self.get_current_zaiko()
        if not zaiko:
            print("その商品は存在しません。在庫を確認してください")
            return

        CURRENT_STOCK = zaiko.stock

        if self.change_stock_num > CURRENT_STOCK:
            print("売上数量に対して在庫が足りません。在庫を確認してください")
            return

        zaiko.stock = CURRENT_STOCK - self.change_stock_num

        session.add(zaiko)
        session.commit()
        print(f"品目{self.id}（単価：{self.unit_price}円）を{self.change_stock_num}{self.unit}売上げました")

def print_all_zaiko():
    zaiko = session.query(TblZaiko.id, MstHinmoku.name, TblZaiko.stock, TblZaiko.unit, TblZaiko.unitprice).join(MstHinmoku, MstHinmoku.id == TblZaiko.id).filter(TblZaiko.stock > 0).all()
    for item in zaiko:
        print(f"品目{item.id}（{item.name}）の在庫：{item.stock}{item.unit}（単価：{item.unitprice}円）")

def main(args):
    """
    メイン関数
    """
    args = sys.argv
    mode = args[1]

    if mode == "1":
        hinmoku = Hinmoku(args[2], args[3])
        return hinmoku.registration_item()
    elif mode == "2":
        transaction = Transaction(args[2], args[3], int(args[4]), int(args[5]))
        return transaction.process_arrival()
    elif mode == "3":
        transaction = Transaction(args[2], args[3], int(args[4]), int(args[5]))
        return transaction.process_sales()
    elif mode == "4":
        return print_all_zaiko()


if __name__ == "__main__":
    main(sys.argv)

