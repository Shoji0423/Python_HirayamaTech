import sys
args = sys.argv

#引数を変数に代入
number = int(args[1])
#タプルの定義
population_list = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")
#国名の出力
print(population_list[number-1],end="")