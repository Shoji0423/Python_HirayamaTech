# price_UseModule.pyのシステムから祝日も考慮するシステム

import sys
import datetime

from database import session
from table import Holiday
# from ..module.func_totalPrice import priceCalc


# 休日判定、大人人数、子供人数を引数にする
def priceCalc(isHoliday, nomal, children):
    
    if isHoliday:
        # 休日の場合の計算
        total_price = nomal * 2400 + children * 1500
    else:
        # 平日の場合の計算
        total_price = nomal * 2000 + children * 1200
    
    return total_price


# 引数をstr型の年月日、int型 大人人数、int型 子供人数として変数に格納
date_str = sys.argv[1]
nomal = int(sys.argv[2])
children = int(sys.argv[3])

# 年月日をそれぞれ分割
year = int(date_str[:4])
month = int(date_str[4:6])
day = int(date_str[6:])

# datetimeモジュールを使って、土日判定
dt = datetime.datetime(year, month, day)
isHoliday = 4 < dt.weekday()

# not土日の状況から祝日判定
if not isHoliday:
    date = datetime.datetime.strptime(date_str, '%Y%m%d')

    # 祝日との一致しているか確認（1回一致しているか）
    flag = session.query(Holiday).filter_by(holi_date=date).count() == 1
    isHoliday = flag

# priceCalcモジュールを使って結果を出力
print(priceCalc(isHoliday, nomal, children), end="円\n")