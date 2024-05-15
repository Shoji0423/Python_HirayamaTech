import sys
args = sys.argv

#引数を変数に代入
number = int(args[1])
sum = 0
while sum < 100:
    sum = sum + number
    if (sum == 100):
        print("Just 100!",end="")
        break
else:
    print("Over!",end="")