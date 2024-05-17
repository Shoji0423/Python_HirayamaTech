# 必要なモジュールをインポート
import sys
import mod.func_salary as csal

# 給与をリストにまとめる
input = sys.argv
incomes = list(map(int, input[1:]))

# 給与を出力する
for i in incomes:
    print(csal.calc_salary(i))