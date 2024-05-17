import sys
args=sys.argv
number=int(args[1])
number_list=[]

while number!=1:
    i=3
    if number % 2==0:
        number=number/2
        number_list.append(2)
    else:
        while True:
            if number % i ==0:
                number=number/i
                number_list.append(i)
                break
            i+=2

print(number_list)
        