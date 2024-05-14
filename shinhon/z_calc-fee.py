children = int(input("子供料金（13才未満）は何人？"))
normal = int(input("通常料金（13-64才）は何人？"))
elder = int(input("年配者料金（65才以上）は何人？"))

total_num = children + normal + elder
children_price = 499
normal_price = 2990
elder_price = 99
children_total_price = children * children_price
normal_total_price = normal * normal_price
elder_total_price = elder * elder_price
total_price = int(children_total_price + normal_total_price + elder_total_price)

if total_num >= 10:
    print("団体割引があります")
    total_price = round(total_price * 0.8)
else:
    print("割引はできません")

print("子供料金　：{0}人 × {1}円 = {2}円".format(children, children_price, children_total_price))
print("通常料金　：{0}人 × {1}円 = {2}円".format(normal, normal_price, normal_total_price))
print("年配者料金：{0}人 × {1}円 = {2}円".format(elder, elder_price, elder_total_price))
print("合計　　　：{0}人 {1}円".format(total_num, total_price))

