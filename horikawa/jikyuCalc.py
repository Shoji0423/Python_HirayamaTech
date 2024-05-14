# 実行後にユーザから入力を受け付け、給料を計算する処理

# 時給の入力
user = input("時給はいくらですか？")
jikyu = int(user)

# 時間の入力
user = input("何時間働きましたか？")
jikan = int(user)

# 給料計算
kyuryou = jikyu * jikan

# 結果を表示
fmt= """
時給が{0}円で、{1}時間働いたので...
時給は、{2}円です。
"""
desc = fmt.format(jikyu, jikan, kyuryou)

print(desc)