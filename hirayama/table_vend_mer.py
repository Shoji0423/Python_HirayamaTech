import sys
from sqlalchemy import Column, String, Date, Integer, Numeric, DateTime
from database import Base
from database import ENGINE

#テーブル：Holidayの定義
class merchandise(Base):
    __tablename__ = 'mst_merchandise'
    id = Column('id', String(10), primary_key = True)
    name = Column('name', String(20))
    price = Column('price', Integer)

    
def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)