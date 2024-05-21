from database import session #データベースへの接続
from tables import Holiday #テーブル定義
import datetime
import sys
args = sys.argv

#引数を変数に代入
date = str(args[1])
adult = int(args[2])
children = int(args[3])

#日付を年・月・日に分割
date_y = int(date[0:4])
date_m = int(date[4:6])
date_d = int(date[6:8])  #str型で分割処理してから、int型に変換

#youbiに入力された日付の曜日をいれる
dt = datetime.date(date_y, date_m, date_d)
youbi = dt.strftime('%a')

#データ取得
Holidaylist = session.query(Holiday.holi_date)

#祝日か判断　if日付がHolidaylistにあれば、その日を祝日と判断する　if 祝日：youbi = shukujitu
#for i in Holidaylistで、一つずつ休日参照
#Holidaylistのholi_date == dateならyoubi = shukujitu
for i in Holidaylist:
    if i.holi_date == dt:
        youbi = "shukujitu"

#合計金額の計算
if youbi == "Sat" or youbi == "Sun" or youbi == "shukujitu": #土日祝
    sum = 2400*adult + 1500*children

else:
    sum = 2000*adult + 1200*children #平日

print(sum)