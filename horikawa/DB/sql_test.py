import sys
from sqlalchemy import Column, String, Date, Integer, Numeric, DateTime
from database import Base
from database import ENGINE

import datetime
from database import session
from aquaattend import Attendnum

date = datetime.datetime.strptime("20240101", '%Y%m%d')
date = date.date()

attendnum = session.query(Attendnum)
print("----------------------------session.query(Attendnum)だと")
print(attendnum)
print("----------------------------こうなる")

attendnum = attendnum.filter_by(entry_date=date)
print("----------------------------session.query(Attendnum).filter_by(entry_date=date)だと")
print(attendnum)
print("----------------------------こうなる")
# session.add(attendnum)
# session.commit()