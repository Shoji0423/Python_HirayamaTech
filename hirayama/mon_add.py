import datetime
from database import session
from table_vend_mon import money
import sys

args=sys.argv
input_price=int(args[1])
number=int(args[2])

attend=money(
    price=input_price,
    number=number
)
session.add(attend)
session.commit()