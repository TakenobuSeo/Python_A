import qrcode
import sys
import os
args = sys.argv
url = args[1]
img_name = str(args[1].split('/')[-2])
img = qrcode.make('QRコードです！')
path = os.path.join("files",img_name)
img.save(path)