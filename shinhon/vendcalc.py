


goods = {
    "お茶": 110,
    "コーヒー": 100,
    "ソーダ": 160,
    "コーンポタージュ": 130,
}

for i in goods:
    print(f"{i}：{goods[i]}")

money_is_enough = 0
while money_is_enough != 3:
    money = input("投入金額を入力してください：")
    if money[-1] != '0':
        print("１円玉、５円玉は使用できません。再度投入金額を入力してください")
    else:
        money_is_enough += 1
    
    money = int(money)
    if money > 10000:
        print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
    else:
        money_is_enough += 1

    for i in goods:
        print(goods[i])
        if money >= goods[i]:
            money_is_enough += 1
        print(f"{index}/{len(goods)}")
        # print(f"{money}円では購入できる商品がありません。再度投入金額を入力してください")
        