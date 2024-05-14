# 引数を"Hello"の後ろにくっつけてprintする処理

import sys
args = sys.argv

# 引数をstr変数に代入
name = args[1]

# 実行
print("Hello " + name + " !",end="")