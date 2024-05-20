from database import session
from tables import Holiday
from datetime import date

# holidaylist = session.query(Holiday).all()
holidaylist = session.query(Holiday).filter(Holiday.holi_date < date(2022, 11, 1))

for item in holidaylist:
    print(item.holi_date, end=" ")
    print(item.holi_text)