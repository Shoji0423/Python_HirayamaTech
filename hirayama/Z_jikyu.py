import sys
#時給の入力
user=input("時給はいくらですか？")
jikyu=int(user)
if jikyu<600 :
    print("労基")
    exit()    
#働いた時間の入力
user=input("何時間働きましたか？")
jikan=int(user)
#給料の計算
kyuryou=jikan*jikyu

fmt="""
時給{0}円で、{1}時間働いたので...
給料は{2}円です。
"""

desc=fmt.format(jikyu,jikan,kyuryou)
print(desc)