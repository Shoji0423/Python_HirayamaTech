import datetime
from database import session
from table_vend_sto import stock
import sys

args=sys.argv
input_id=int(args[1])
zaiko=int(args[2])

attend=stock(
    id=input_id,
    stock=zaiko
)
session.add(attend)
session.commit()