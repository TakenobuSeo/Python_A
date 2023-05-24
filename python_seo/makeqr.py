import os
import qrcode

path = os.path.join("../..", "files", "lunasea.png")
img = qrcode.make("https://www.lunasea.jp/")

img.save(path)