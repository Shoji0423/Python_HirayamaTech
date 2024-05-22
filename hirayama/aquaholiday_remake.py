import sys
import datetime
from database import session
from tables import Holiday
args=sys.argv
#日付・大人・子供の人数を入力
day=args[1]
adult=int(args[2])
child=int(args[3])
#祝日の名前と日付を取得
holiday_list=session.query(Holiday).all()
#日付型に変換
day=datetime.datetime.strptime(day,'%Y%m%d')

#料金を計算する処理#
########################################################
#土日か判定
if day.strftime("%a") =="Sat" or day.strftime("%a") =="Sun":
    sum=adult*2400+child*1500
else:
    sum=adult*2000+child*1200
    #祝日か判定
    for item in holiday_list:
        if day == item.holi_date.strftime('%Y%m%d'):
            sum=adult*2400+child*1500
            break
########################################################
print(sum,end="")



