# 第2引数で指定したURLを第3引数のファイル名でQRコードとして保存する処理
# 保存場所は /home/matcha-23training/projects/python/files

import qrcode
import os
import sys

link = sys.argv[1]
fileName = sys.argv[2]



# QRコードを生成
img = qrcode.make(link)

path = os.path.join("..","..","files", fileName)

img.save(path)