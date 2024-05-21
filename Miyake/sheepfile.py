import sys
args = sys.argv

#引数を変数に代入
number = int(args[1])

a_file = open("sheep.txt", mode="w", encoding="utf-8")
for i in range(1,number+1):
    a_file.write("ひつじが{0}匹".format(i))
    if i > 200:
        break

a_file.close()
#スライド106の部分まだできてない！