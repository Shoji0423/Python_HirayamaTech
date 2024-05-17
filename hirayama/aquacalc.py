import sys
import datetime

args=sys.argv
day=args[1]
old=int(args[2])
child=int(args[3])
t=datetime.datetime.strptime(day,'%Y%m%d')

if t.strftime("%a") =="Sat" or t.strftime("%a") =="Sun":
    sum=old*2400+child*1500
else:
    sum=old*2000+child*1200

print(sum,end="")



