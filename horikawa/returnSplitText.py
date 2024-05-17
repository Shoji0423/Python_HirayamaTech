# 引数で受け付けた文字列の空白を区切り文字として処理を行い、単語単位で分割する
# 第3引数で指定された番号の単語を返す処理

import sys

# 第2引数の文字列を単語単位で分割する処理
text_Array = sys.argv[1].split()

# 返す単語の番号
returnNum = int(sys.argv[2]) - 1

# 答えを返す
print(text_Array[returnNum],end="")