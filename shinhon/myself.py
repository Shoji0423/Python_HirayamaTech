from mod.introduce import Intro #自己紹介の文を出すツール
import sys

# 必要な情報を代入する
input = sys.argv
name = str(input[1])
age = str(input[2])

# Introのインスタンスを作成し、名前をプリントする
user = Intro(name, age)
print(user.name_out())
print(user.age_out())