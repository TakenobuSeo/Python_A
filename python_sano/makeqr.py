import sys
import os
import qrcode

args = sys.argv
path = os.path.join("..","files", f"{args[2]}.png")

img = qrcode.make(args[1])
img.save(path)

# with open(path, mode="w", encoding="utf-8") as f:
    