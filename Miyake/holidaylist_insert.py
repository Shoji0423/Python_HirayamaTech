from datetime import date
from database import session #データベースへの接続
from tables import Holiday #テーブル定義

#登録するデータの編集
holiday = Holiday(
    holi_date = date(2023, 1, 1),
    holi_text = "お正月"
)
#INSERT処理
session.add(holiday)
#コミット
session.commit()

