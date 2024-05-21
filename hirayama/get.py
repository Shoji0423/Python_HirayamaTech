from database import session
from tables import Holiday

holilist=session.query(Holiday).all()
for item in holilist:
    print(item.holi_date)
    print(item.holi_text)