import sys
args = sys.argv

#引数を変数に代入
food_name = args[1]
print("I don't like \""+food_name+"\"",end="")
#print("I don't like \"",food_name,"\"",end="")だと半角が入ってしまう（I don't like ”△嫌いな食べ物△”）