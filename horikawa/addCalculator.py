# 3つの整数を引数として、その合計を返す処理

import sys
args = sys.argv

# 3つの変数を格納
num1 = int(args[1])
num2 = int(args[2])
num3 = int(args[3])

# 足し算を実行
print(num1 + num2 + num3,end="")