
import sys
# 最大数
max_count = int(sys.argv[1])

# ループ実行回数
count = 0

sheep_file = open("../../files/sheep.txt", mode="w", encoding="utf-8")
# 0スタートで1匹ずつ増えるループ
while count < max_count:
    count += 1
    sheep_file.write("ひつじが{0}匹\n".format(count))

sheep_file.close()