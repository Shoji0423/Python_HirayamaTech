import datetime
from database import session
from table_atten import attend
import sys

args=sys.argv
day=args[1]
adult_data=int(args[2])
child_data=int(args[3])

date=datetime.datetime.strptime(day,'%Y%m%d')
date = date.date()

count=session.query(attend.entry_date).filter_by(entry_date=date).count()
attend=attend(
    entry_date=date,
    seq=int(count)+1,
    adult=adult_data,
    child=child_data
)
session.add(attend)
session.commit()