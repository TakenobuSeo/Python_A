import sys
from sqlalchemy import Column, String, Date, Integer
from database import Base
from database import ENGINE

#テーブル：Holidayの定義
class Holiday(Base):
    __tablename__ = 'holiday'
    holi_date = Column('holi_date', Date, primary_key = True)
    holi_text = Column('holi_text', String(20))


class MstMerchandise(Base):
    __tablename__ = 'mst_merchandise'
    id = Column('id', String(10), primary_key = True)
    name= Column('name', String(20))
    price= Column('price', Integer)

class TblStock(Base):
    __tablename__ = 'tbl_stock'
    id = Column('id', String(10), primary_key = True)
    stock= Column('stock', Integer)

class TblMoney(Base):
    __tablename__ = 'tbl_money'
    price= Column('price', Integer, primary_key = True)
    number = Column('number', Integer)

class TblMessage(Base):
    __tablename__ = 'tbl_message'
    seq = Column('seq', Integer,autoincrement=True, primary_key = True)
    message= Column('message', String(100))
    datetime= Column('datetime', Date)

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)