import sys
args=sys.argv
number=int(args[1])
#タプルを定義
kuni=("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")
#指定された国を出力
print(kuni[number-1])