# 時給計算プログラム

# jikyuに入力した数値を代入
user = input("時給はいくらですか？")
jikyu = int(user)

# jikanに入力した数値を代入
user = input("何時間働きましたか？")
jikan = int(user)

# 給料を算出
kyuryou = jikyu * jikan

# 結果を表示
fmt = """
時給は{0}円で、{1}時間働いたので、、、
給料は、{2}円です。
"""
desc = fmt.format(jikyu, jikan, kyuryou)
print(desc)