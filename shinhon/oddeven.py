# inputに引数を代入
import sys
input = int(sys.argv[1])

# 奇数か偶数の結果を出力する
if input % 2:
    print("奇数", end="")
else:
    print("偶数", end="")