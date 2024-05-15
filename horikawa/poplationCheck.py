# 世界人口ランキングを格納したリストから、入力で受け付けた数値の順位の国を返す処理

import sys
selectNum = int(sys.argv[1]) - 1

# 人口ランキングリスト
poplotionList = ["China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico"]

# 結果を返す
print(poplotionList[selectNum], end="")