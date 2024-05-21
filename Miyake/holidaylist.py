from database import session #データベースへの接続
from tables import Holiday #テーブル定義

Holidaylist = session.query(Holiday).all()

for i in Holidaylist:
    print(i.holi_date,end=" ")
    print(i.holi_text)