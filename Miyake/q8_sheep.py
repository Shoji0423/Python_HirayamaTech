import sys
args = sys.argv

#引数を変数に代入
number = int(args[1])

if number < 200:
    for i in range(number):
        print("羊が",i+1,"匹")