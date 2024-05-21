import sys
from sqlalchemy import Column, String, Date, Integer, Numeric, DateTime
from database import Base
from database import ENGINE

#テーブル：Holidayの定義
class money(Base):
    __tablename__ = 'tbl_money'
    price = Column('price', Integer,primary_key = True)
    number = Column('number', Integer)

    
def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)