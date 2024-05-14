# 3教科の点数を引数とし、全て70点以上or合計220点以上の場合、合格を返す処理
# ただし、50点未満の点数がある場合は不合格
import sys
agrs = sys.argv

# 数学、国語、英語の点数を変数へ格納
math = int(agrs[1])
japanese = int(agrs[2])
english = int(agrs[3])

# 合格判定変数
check_bool = False

# 合格条件の判定
if math >= 70 and japanese >= 70 and english >= 70:
    check_bool = True
elif math + japanese + english >= 220:
    check_bool = True

# 不合格条件の判定
if math < 50 or japanese < 50 or english < 50:
    check_bool = False

# 合格不合格を返す
if check_bool:
    print("合格", end="")
else:
    print("不合格",end="")