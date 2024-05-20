# introFamily.pyを使って、猫の名前を第4引数で受け取って猫の名前も紹介する処理

from module.introFamily import IntroFam
import sys

# 人の名前、氏名、猫の名前を登録
name = sys.argv[1]
age = sys.argv[2]
cat_name = sys.argv[3]

# IntroFamクラスを作成
myself = IntroFam(name,age,cat_name)

# 結果を出力
print(myself.name_out())
print(myself.age_out())
print(myself.cat_out())