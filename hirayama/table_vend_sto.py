import sys
from sqlalchemy import Column, String, Date, Integer, Numeric, DateTime
from database import Base
from database import ENGINE

#テーブル：Holidayの定義
class stock(Base):
    __tablename__ = 'tbl_stock'
    id = Column('id', String(10), primary_key = True)
    stock = Column('stock', Integer)

    
def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)