from database import session
from table import Holiday

# データを書き換える処理 "休日"を"振替休日"に

holiday = session.query(Holiday).filter_by(holi_text="休日").all()

for item in holiday:
    item.holi_text = "振替休日"
    session.add(item)

session.commit()

# holidayテーブルに格納されたデータ（休日）を全て表示する処理
holidaylist = session.query(Holiday).all()

for holiday in holidaylist:
    print(str(holiday.holi_date) + " " + holiday.holi_text)
# print(holidaylist)