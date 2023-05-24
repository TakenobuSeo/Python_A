import sys
from sqlalchemy import Column, String, Date, Integer
from database import Base
from database import ENGINE

class Holiday(Base):
    """テーブル：Holidayの定義"""
    __tablename__ = 'holiday'
    holi_date = Column('holi_date', Date, primary_key = True)
    holi_text = Column('holi_text', String(20))

class MstMerchadise(Base):
    """テーブル：mst_merchandiseの定義"""
    __tablename__ = "mst_merchandise"
    id = Column('id', String(10), primary_key = True)
    name = Column('name', String(20))
    price = Column('price', Integer)

class TblStock(Base):
    """テーブル：tbl_stockの定義"""
    __tablename__ = "tbl_stock"
    id = Column('id', String(10), primary_key = True)
    stock = Column('stock', Integer)

class TblMoney(Base):
    """テーブル：tbl_moneyの定義"""
    __tablename__ = "tbl_money"
    price = Column('price', Integer, primary_key = True)
    number = Column('number', Integer)

class TblMessage(Base):
    """テーブル：tbl_messageの定義"""
    __tablename__ = "tbl_message"
    seq = Column('seq', Integer, primary_key = True)
    message = Column('message', String(100))
    datetime = Column('datetime', Date)



def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)