import qrcode
import sys
import os

link = str(sys.argv[1])

img = qrcode.make(link)

print(os.path)
print(os.path.join("../..", "files", "qrcode.png"))

img.save(os.path.join("../..", "files", "qrcode.png"))