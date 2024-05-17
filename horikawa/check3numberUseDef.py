import sys
numList = sys.argv

# str型で登録された引数の配列をint型へ変換してnumListへ格納
numList.pop(0)
numList = map(int, numList)

#関数を定義
def calcvalue(num):
    #あまりを算出
    mod = num % 2

    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

for i in numList:
    calcvalue(i)