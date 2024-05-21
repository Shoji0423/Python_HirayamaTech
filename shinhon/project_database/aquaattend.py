# 必要なパッケージとモジュールをインポート
from database import session #databaseへの接続
from tables import Attendnum #テーブルへのアクセス
from func_aquacalc import output_date #日付を出力するモジュール
import sys

# インプットを整理する
input = sys.argv
input_date = str(input[1])
input_adult = int(input[2])
input_child = int(input[3])

# dateの出力
entry_date = output_date(input_date)

# 同じ日付の注文の数を調べて、seqの番号を決める
select_entries = session.query(Attendnum).filter(Attendnum.entry_date == entry_date)
count_seq = select_entries.count() + 1

# Databaseに入れるデータの作成と登録
purchase = Attendnum(
    entry_date = entry_date,
    seq = count_seq,
    adult = input_adult,
    child = input_child,
)

session.add(purchase)
session.commit()