import sys
args=sys.argv
number=[]
number.append(int(args[1]))
number.append(int(args[2]))
number.append(int(args[3]))

def calcvalue(num) :
    for i in num:
        if i % 2==0:
            print(str(i)+"は偶数")
        else:
            print(str(i)+"は奇数")
    
calcvalue(number)