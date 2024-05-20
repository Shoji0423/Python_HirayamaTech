# yyymmmdd形式で日程入力を受け付け、曜日によって変わる遊園地の料金と大人子供の人数から、
# 合計金額を算出する処理

import sys
import datetime

from module.func_totalPrice import priceCalc

# 引数をstr型の年月日、int型 大人人数、int型 子供人数として変数に格納
date = sys.argv[1]
nomal = int(sys.argv[2])
children = int(sys.argv[3])

# 年月日をそれぞれ分割
year = int(date[:4])
month = int(date[4:6])
day = int(date[6:])

# datetimeモジュールを使って、土日判定
dt = datetime.datetime(year, month, day)
isHoliday = 4 < dt.weekday()

# priceCalcモジュールを使って結果を出力
print(priceCalc(isHoliday, nomal, children), end="")