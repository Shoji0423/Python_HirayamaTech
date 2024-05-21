import sys
import datetime
from database import session
from tables import Holiday

args=sys.argv
day=args[1]
old=int(args[2])
child=int(args[3])
holilist=session.query(Holiday).all()

for item in holilist:
    print(item.holi_date.strftime('%Y%m%d'))
    if day == item.holi_date.strftime('%Y%m%d'):
        flg=1
        
t=datetime.datetime.strptime(day,'%Y%m%d')

if t.strftime("%a") =="Sat" or t.strftime("%a") =="Sun":
    sum=old*2400+child*1500
elif flg==1:

    sum=old*2400+child*1500
else:
    sum=old*2000+child*1200

print(sum,end="")



