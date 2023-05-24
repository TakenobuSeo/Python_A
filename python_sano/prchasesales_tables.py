import sys
from sqlalchemy import Column, String, Date, Integer
from database import Base
from database import ENGINE

class MstHinmoku(Base):
    """テーブル：mst_hinmokuの定義"""
    __tablename__ = 'mst_hinmoku'
    id = Column('id', String(10), primary_key = True)
    name = Column('name', String(20))

class TblZaiko(Base):
    """テーブル：tbl_zaikoの定義"""
    __tablename__ = 'tbl_zaiko'
    id = Column('id', String(10), primary_key = True)
    unit = Column('unit', String(10), primary_key = True)
    unitprice = Column('unitprice', Integer, primary_key = True)
    stock = Column('stock', Integer)

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)