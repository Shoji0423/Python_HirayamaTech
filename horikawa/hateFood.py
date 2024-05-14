# 入力した引数を「嫌いな食べ物の説明文」として返す処理
import sys
args=sys.argv

food=args[1]

# 実行
print("I don't like \"" + food + "\"",end="")