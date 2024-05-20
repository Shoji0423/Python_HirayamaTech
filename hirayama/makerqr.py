import os
import qrcode
import sys
args=sys.argv
ur=args[1]
filename=args[2]
img=qrcode.make(ur)
path=os.path.join("../../files",filename)
print(path)
img.save(path)