# 動物リストを操作する処理
# 第2引数：追加するインデックスの位置（数値）
# 第3引数：追加する動物名
# [1]リストの末尾要素を削除 & [2]リストを昇順にソート

import sys
# 追加するインデックス番号と要素
num = int(sys.argv[1])
name = sys.argv[2]

animalList = ["giraffe", "tiger", "zebra", "elephant", "lion"]

animalList.insert(num,name) # 要素追加
animalList.pop()            # [1]

animalList.sort()           # [2]

# 結果を表示
print(animalList, end="")

