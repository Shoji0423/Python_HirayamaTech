# 子供・大人の3区分の料金設定を設け、それぞれの人数の入力を受け付けた後に、合計金額を返す処理
# モジュール

"""
料金表
        平日    休日
大人    2000    2400
子供    1200    1500
"""

# 祝日判定、大人人数、子供人数を引数にする
def priceCalc(isHoliday, nomal, children):
    
    if isHoliday:
        # 祝日の場合の計算
        total_price = nomal * 2400 + children * 1500
    else:
        # 平日の場合の計算
        total_price = nomal * 2000 + children * 1200
    
    return total_price