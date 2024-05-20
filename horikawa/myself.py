# クラスを使って自己紹介のテキストを出力する処理
# 第2引数に名前、第3引数に年齢を渡す

from module.introduce import Intro
import sys

name = sys.argv[1]
age = sys.argv[2]

myself = Intro(name,age)

print(myself.name_out())
print(myself.age_out())