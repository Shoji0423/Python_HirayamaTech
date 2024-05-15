import sys
args=sys.argv
number=int(args[1])
sum=0
while sum <= 100 :
    sum+=number
    if sum == 100:
        print("Just 100!" ,end="")
        break
else:
    print("Over!",end="")