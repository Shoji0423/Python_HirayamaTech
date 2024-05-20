import sys
import qrcode
import os

args = sys.argv

#引数を変数に代入
url = args[1]              
filename = args[2]

img = qrcode.make(url)

path = os.path.join("../../","files", filename)
img.save(path)