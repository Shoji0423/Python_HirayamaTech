# 子供・大人・年配者の3区分の料金設定を設け、それぞれの人数の入力を受け付けた後に、合計金額を返す処理

# 人数入力
children = int(input("子供料金(13歳未満)は何人 ? "))
normal = int(input("通常料金(13~64歳)は何人 ? "))
elder = int(input("年配者料金(65歳以上)は何人 ? "))

# 集計
total_count = children + normal + elder

children_price = children * 500
normal_price = normal * 1000
elder_price = elder * 700

total_price = children_price + normal_price + elder_price

# 割引判定
if total_count >= 10:
    print("団体割引が適用されます")
    total_price *= 0.8
else:
    print("団体割引は適用されません")

# 結果を返す
print("子供料金　:{0}人× 500= {1}円".format(children, children_price))
print("通常料金　:{0}人×1000= {1}円".format(normal, normal_price))
print("年配者料金:{0}人× 700= {1}円".format(elder, elder_price))

print("合計: {0}人{1}円".format(total_count, total_price))