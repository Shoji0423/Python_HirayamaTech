import sys
yn="Y"
drink_list={"お茶":110,"コーヒー":100,"ソーダ":160,"コンポタージュ":130}
for name in drink_list:
    print(name+"："+str(drink_list[name])+"円")
money=int(input("投入金額を入力してください"))

#金額入力フェーズ
while True :
    #何も買えない場合
    if min(drink_list.values())>money :
        money=int(input(str(money)+"円では購入できる商品がありません。再度投入金額を入力してください"))
    #10000以上を入力した場合
    elif money > 10000 :
        money=int(input("10000円を超える金額は投入できません。再度投入金額を入力してください"))
    #1円玉もしくは5円玉を投入しようとしている場合
    elif money%10!=0:
        money=int(input("1円玉、5円玉は使用できません。再度金額を入力してください"))
    else:
        break
    
#購入フェーズ
while True:
    input_syo=input("何を購入しますか（商品名/cancel）")
    #cancelが入力された場合購入フェーズを抜ける
    if input_syo=="cancel" :
        break
    else:
        money=money-drink_list[input_syo]
    #最安値以上残高が残っている場合
    if min(drink_list.values())<=money:
        print("残金："+str(money)+"円")
        yn=input("続けて購入しますか(Y/N)")
    else:
        break
    if yn=="N":
        break
    for name in drink_list:
        print(name+str(drink_list[name])+"円")
        
#おつりフェーズ 
print("おつり")
if money >= 1000:
    print("1000円札："+str(int(money/1000))+"枚")
    money=money%1000
if money >= 500:

    print("500円玉："+str(int(money/500))+"枚")
    money=money%500
if money >= 100:
    print("100円玉："+str(int(money/100))+"枚")
    money=money%100
if money >= 50:
    print("50円玉："+str(int(money/50))+"枚")
    money=money%50
if money >= 10:
    print("10円玉："+str(int(money/10))+"枚")
         
    


    