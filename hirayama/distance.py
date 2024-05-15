import sys
args=sys.argv
basyo1=args[1]
basyo2=args[2]
#駅名と距離の辞書を定義
station={"東京":0.00,"品川":6.78,"新横浜":25.54,"名古屋":342.02,"京都":476.31,"新大阪":515.35}
#東京駅からの距離を出力
print(round(abs(station[basyo1]-station[basyo2]),2))