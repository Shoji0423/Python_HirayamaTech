# 給与額の入力を受け付け、"支給額"と"税額"を返す
# 100万以下は税率10%, 100万以上は超えた部分が税率20%

# 税率の変わる給与額を変数で管理して、税率を計算

import sys
import module.func_salary as csal

# 入力されたリストを給与額のリストに格納
salaryList = sys.argv

# 引数の先頭(実行ファイル名)の要素を削除
salaryList.pop(0)

salaryList = list(map(int, salaryList))

for salary in salaryList:
    csal.salaryCalc(salary)