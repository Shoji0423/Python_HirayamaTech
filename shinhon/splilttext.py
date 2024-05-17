# テキストと切り出す番号を代入
import sys
text = sys.argv[1]
num = int(sys.argv[2])

# 結果を出力する
output = text.split()[num-1]
print(output)