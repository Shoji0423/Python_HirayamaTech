# 必要なものをインポートする
import sys
from decimal import Decimal, ROUND_HALF_UP

# 始発駅と到着駅の文字を代入する
start = sys.argv[1]
end = sys.argv[2]

# 駅のデータ
stations = {
    "東京": 0.00,
    "品川": 6.78,
    "新横浜": 25.54,
    "名古屋": 342.02,
    "京都": 476.31,
    "新大阪": 515.35
}

# 駅が存在しているかどうかを確認する
try:
    start_dis = stations[start]
    end_dis = stations[end]
    print(Decimal(abs(end_dis - start_dis)).quantize(Decimal(".01"), rounding=ROUND_HALF_UP))
except:
    print('のぞみの停車駅を引数に設定してください')