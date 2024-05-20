from datetime import date
from database import session
from tables import Holiday

holiday = Holiday(
    holi_date = date(2024, 4, 1),
    holi_text = "シャチクの日"
)

session.add(holiday)
session.commit()
