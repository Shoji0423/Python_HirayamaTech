# 引数を代入
import sys
score_list = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]

total_score = sum(score_list)

# 出力する
if all(ele >= 70 for ele in score_list):
    print("合格", end="")
elif all(ele >= 50 for ele in score_list) and total_score >= 220:
    print("合格", end="")
else:
    print("不合格", end="")