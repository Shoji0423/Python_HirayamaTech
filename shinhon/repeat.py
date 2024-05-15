# 代入
import sys
count = int(sys.argv[1])

# 計算と出力
addCount = 0
while addCount < 100:
    addCount = addCount + count
    if addCount == 100:
        print("Just 100!", end="")
        break;
else:
    print("Over!", end="")