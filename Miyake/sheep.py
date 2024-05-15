import sys
args = sys.argv

#引数を変数に代入
number = int(args[1])

for i in range(1,number+1):
    print("ひつじが{0}匹".format(i))
    if i > 200:
        break