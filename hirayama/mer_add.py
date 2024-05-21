import datetime
from database import session
from table_vend_mer import merchandise
import sys

args=sys.argv
name1=args[1]
price1=int(args[2])
count=session.query(merchandise.id).count()
attend=merchandise(
    id=count,
    name=name1,
    price=price1
)
session.add(attend)
session.commit()