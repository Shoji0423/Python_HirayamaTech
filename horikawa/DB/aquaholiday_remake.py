# price_UseModule.pyのシステムから祝日も考慮するシステム
import sys
import datetime

from database import session
from table import Holiday

def priceCalc(isHoliday:bool, adult:int, child:int):
    '''
    平日・休日別で合計料金を算出。
    '''
    # 休日の場合の計算
    if isHoliday: total_price = adult * 2400 + child * 1500
    # 平日の場合の計算
    else: total_price = adult * 2000 + child * 1200
    
    return total_price


# sysの引数を格納
date_str = sys.argv[1]  # str型:年月日
nomal,children = int(sys.argv[2]), int(sys.argv[3]) # int型:大人人数,int型:子供人数

# 年月日をそれぞれ分割
year,month,day = int(date_str[:4]),int(date_str[4:6]),int(date_str[6:])

# datetimeモジュールを使って、土日判定 https://kino-code.com/python-datetime-weekday/
dt = datetime.datetime(year,month,day)
isHoliday = 4 < dt.weekday()

# 土日ではない祝日の判定
if not isHoliday:
    # str型の日付をdate型へ変換
    date = datetime.datetime.strptime(date_str, '%Y%m%d')

    # 祝日との一致しているか確認（1回一致しているか）
    flag = session.query(Holiday).filter_by(holi_date=date).count() == 1
    isHoliday = flag

# priceCalc関数を使って結果を出力
print(priceCalc(isHoliday, nomal, children), end="円\n")