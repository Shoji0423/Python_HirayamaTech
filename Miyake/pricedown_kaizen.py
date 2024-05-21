#値下げした金額を表示するプログラム

import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]              #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")            #果物類をタプルで定義
alcohol = ("ビール", "日本酒")                         #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

#関数内で値下げ計算を行う
def keisan(kubun):
    for food in kubun:
        hinmoku[food] = hinmoku[food] - price_down
        #値下げ後の金額が1円未満の場合は、1円とする
        if hinmoku[food] < 0:
            hinmoku[food] = 1

#どの区分か判断する
if hm_class == "果物類":
    keisan(fruits)
elif hm_class == "酒類":
    keisan(alcohol)
elif hm_class == "麺類":
    keisan(noodles)

print(hinmoku,end="")
