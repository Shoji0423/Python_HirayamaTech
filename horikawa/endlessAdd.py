# 入力された数値を足すループ処理
# ちょうど100なら「Just 100!」、超えたら「Over!」と表示して終了

import sys
# 基盤の数値、合計
baseNum = int(sys.argv[1])
sum = 0

while sum < 100:
    sum += baseNum

    # 判定　100ぴったり
    if sum == 100:
        print("Just 100!", end="")
    # 判定　100オーバー
    elif sum > 100:
        print("Over!", end="")
