# 必要なモジュールをインポートする
import datetime
import sys

# 引数を代入
input = sys.argv

# 日付と人数を抽出
str_date = input[1]
adult = int(input[2])
child = int(input[3])

# 日付型に変換
dt = datetime.date(int(str_date[:4]), int(str_date[4:6]), int(str_date[6:]))

# 平日と土日の料金
tickets_weekend = {
    "大人": 2400,
    "子供": 1500
}

tickets_normal = {
    "大人": 2000,
    "子供": 1200
}

def calc_price(date_list, a, c):
    '''合計金額を算出する関数'''
    return date_list["大人"] * a + date_list["子供"] * c

# 日付が正しいかどうかを確認
if datetime.date(2022,1,1) <= dt <= datetime.date(2022,12,31):
    # 人数が正しいかどうかを確認
    if 0 <= adult <= 20 and 0 <= child <= 20:
        # 土日か平日かを判断
        if int(dt.strftime('%w')) == 0 or int(dt.strftime('%w')) == 6:
            print(calc_price(tickets_weekend, adult, child))
        else:
            print(calc_price(tickets_normal, adult, child))
    else:
        print("正しい人数を指定してください: 0人 ~ 20人")
else:
    print("正しい日付を入力してください: 20220101 - 20221231")