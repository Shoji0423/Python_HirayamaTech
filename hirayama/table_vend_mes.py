import sys
from sqlalchemy import Column, String, Date, Integer, Numeric, DateTime
from database import Base
from database import ENGINE

#テーブル：Holidayの定義
class message(Base):
    __tablename__ = 'tbl_message'
    seq = Column('seq', Integer, primary_key = True)
    Message = Column('message', String(100))
    datetime = Column('datetime', DateTime)

    
def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)