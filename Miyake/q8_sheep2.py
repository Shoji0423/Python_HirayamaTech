import sys
args = sys.argv

#引数を変数に代入
number = int(args[1])
i = 1

if number < 200:
    while i <= number:
        print("羊が",i,"匹")
        i = i + 1


