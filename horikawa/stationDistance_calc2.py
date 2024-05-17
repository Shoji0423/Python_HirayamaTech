# 辞書データ[新幹線駅名：東京駅との距離]から、2つの引数の駅間の距離を返す処理
# 出力条件：小数第2位まで

# 追加機能：例外処理の実装

import sys

# 辞書データ[新幹線駅名：東京駅との距離]
stationDic = {
    "東京"   :   0.00,
    "品川"   :   6.78,
    "新横浜" :  25.54,
    "名古屋" : 342.02,
    "京都"   : 476.31,
    "新大阪" : 515.35
}

# 2つの駅の距離を計算し、表示する関数
def calcDistance(name_A, name_B):
    # # 2つの駅、それぞれの東京間の距離を格納
    station_A = stationDic[name_A]
    station_B = stationDic[name_B]

    # 距離の計算
    if station_A > station_B:
        answer = station_A - station_B
    else:
        answer = station_B - station_A

    # 結果を少数第2位までで出力
    print("{:.2f}".format(answer),end="")

# 辞書データの中にnameの要素があるかどうか、確認しbool変数で返す処理
def checkInDic(name):
    return name in stationDic

name_A = sys.argv[1]
name_B = sys.argv[2]

# 駅名が存在するか判定
if checkInDic(name_A) and checkInDic(name_B):
    calcDistance(name_A, name_B)
else:
    print("のぞみの停車駅を引数に設定してください", end="")