# 入力された数字に到達するまで羊を数える

# whileループで実施
import sys

# 最大数
max_count = int(sys.argv[1])

# ループ実行回数
count = 0

# 0スタートで1匹ずつ増えるループ
while count < max_count:
    count += 1
    print("ひつじが{0}匹".format(count))