from database import session #データベースへの接続
from attendnum_tables import Attendnum #テーブル定義
import datetime
import sys
args = sys.argv

#引数を変数に代入
date = str(args[1])
adult_num = int(args[2])
child_num = int(args[3])

#日付を年・月・日に分割
date_y = int(date[0:4])
date_m = int(date[4:6])
date_d = int(date[6:8])  #str型で分割処理してから、int型に変換

dt = datetime.date(date_y, date_m, date_d)

#テーブルリスト参照
attendlist = session.query(Attendnum.entry_date)

renban = 1
#連番かどうか判断
for i in attendlist:
    if i.entry_date == dt:
        renban = renban + 1

#テーブル（attendnum）にデータを追加
attendnum = Attendnum(
    entry_date = dt,
    seq = renban,
    adult = adult_num,
    child = child_num
)

session.add(attendnum)  #INSERT処理
session.commit()  #コミット
