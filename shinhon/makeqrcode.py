import qrcode #Qrcodeを作成するためのツール
import sys
import os #ローカルのパスを把握するためのツール

# リンクとファイル名を定義
link = str(sys.argv[1])
filename = str(sys.argv[2])

img = qrcode.make(link)

img.save(os.path.join("../..", "files", filename))