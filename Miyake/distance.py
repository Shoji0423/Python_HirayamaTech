import sys
from decimal import Decimal, ROUND_HALF_UP
args = sys.argv

#引数を変数に代入
station_name1 = str(args[1])
station_name2 = str(args[2])
#辞書の定義
station = {'東京':0.00, '品川':6.78, '新横浜':25.54, '名古屋':342.02, '京都':476.31, '新大阪':515.35}

#東京駅からの距離がstation_name1の方がstation_name2よりも近い場合
if station[station_name1] < station[station_name2]:
    distance = station[station_name2] - station[station_name1]
#東京駅からの距離がstation_name2の方がstation_name1よりも近い場合
elif station[station_name1] > station[station_name2]:
    distance = station[station_name1] - station[station_name2]
#距離の計算
distance = Decimal(str(distance)).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)
print(distance,end="")