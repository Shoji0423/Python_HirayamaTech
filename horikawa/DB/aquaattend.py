import sys
from sqlalchemy import Column, String, Date, Integer, Numeric, DateTime
from database import Base
from database import ENGINE

import datetime
from database import session
from table import Holiday

#テーブル：Attendnumの定義 

class Attendnum(Base):
    __tablename__ = 'attendnum'
    entry_date = Column('entry_date', Date, primary_key = True)
    seq = Column('seq', Integer, primary_key = True)
    adult = Column('adult', Integer)
    child = Column('child', Integer)

# 実行済みなのでコメントアウト
# def main(args):
#     """
#     メイン関数
#     """
#     Base.metadata.create_all(bind=ENGINE)

# if __name__ == "__main__":
#         main(sys.argv)


# 引数をstr型の年月日、int型 大人人数、int型 子供人数として変数に格納
# date_str = sys.argv[1]
# normal = int(sys.argv[2])
# children = int(sys.argv[3])

# # # str型の日付をdate型へ変換 & 年月日のみの表示
# date = datetime.datetime.strptime(date_str, '%Y%m%d')
# date = date.date()

# # 入力予定の日付の重複回数をカウントし、1を足す
# count = session.query(Attendnum).filter_by(entry_date=date).count() + 1

# # データの登録
# attendnum = Attendnum(
#     entry_date = date,
#     seq = count,
#     adult = normal,
#     child = children
# )
# session.add(attendnum)
# session.commit()

# attendnum = session.query(Attendnum).filter_by(entry_date=date).first()
# attendnum.seq = 1
# # print("↓")
# # print(attendnum)
# # print("ここまで")
# session.add(attendnum)
# session.commit()