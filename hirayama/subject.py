import sys
args=sys.argv
ma=int(args[1])
ja=int(args[2])
en=int(args[3])
#3教科とも70点以上、もしくは合計点数が220点以上か？
if ma >= 70 and ja >= 70 and en >= 70 or ma+ja+en >= 220:
    #3教科とも50点以上か判定
    if ma >= 50 and ja >= 50 and en >= 50:
        print("合格",end="")
        exit()
print("不合格",end="")
