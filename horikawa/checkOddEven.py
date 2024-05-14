# 引数の整数を奇数偶数判定を行い、その結果を返す処理
import sys
args = sys.argv

# 判定用変数
checkNum = int(args[1])

# 判定処理
if(checkNum % 2 == 0):
    addEven = "偶数"
else:
    addEven = "奇数"

print(addEven,end="")