from datetime import date
from database import session
from tables import Attendnum

import sys

input = sys.argv
input_date = str(input[1])
adult = int(input[2])
child = int(input[3])

entry_date = date(int(input_date[:4]), int(input_date[4:6]), int(input_date[6:]))

select_entries = session.query(Attendnum).filter(Attendnum.entry_date == entry_date)

seq = select_entries.count() + 1

purchase = Attendnum(
    entry_date = entry_date,
    seq = seq,
    adult = adult,
    child = child,
)

session.add(purchase)
session.commit()