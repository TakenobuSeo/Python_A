import sys
args = sys.argv

# 引数を数値型に変換
num = int(args[1])

i = 2

while i <= num:
    num = num / i
