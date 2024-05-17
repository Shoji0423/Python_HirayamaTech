
#複数の整数の奇数・偶数を判定する

import sys
args = sys.argv

#引数を変数に代入
num1 = int(args[1])
num2 = int(args[2])
num3 = int(args[3])

#関数
def calcvalue(number):
    if -2000000000 <= number <= 2000000000: 
        #偶数の場合
        if number % 2 == 0:
            print("{0}は偶数".format(number))
        #奇数の場合
        else:
            print("{0}は奇数".format(number))

calcvalue(num1)
calcvalue(num2)
calcvalue(num3)