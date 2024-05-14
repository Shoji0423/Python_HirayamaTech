import sys
args=sys.argv
number=args[1]
#偶数奇数判定
if int(number) % 2 == 0 :
    #余りが0だった場合、偶数
    print("偶数",end="")
else:
    #余りが1だった場合、奇数
    print("奇数",end="")