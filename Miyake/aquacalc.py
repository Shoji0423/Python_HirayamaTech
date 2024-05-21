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

#平日か土日祝か判断
dt = datetime.date(date_y, date_m, date_d)
youbi = dt.strftime('%a')

#合計金額の計算
if youbi == "Sat" or youbi == "Sun": #土日
    sum = 2400*adult + 1500*children

else:
    sum = 2000*adult + 1200*children #平日

print(sum)