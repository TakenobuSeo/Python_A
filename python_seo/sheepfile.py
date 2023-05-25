import sys
args = sys.argv

# 引数を数値型に変換
num = int(args[1])

for i in range(1, num+1):
    with open("../../files/sheep.txt", mode="w" ,encoding="utf-8") as s:
        s.write("ひつじが{sheep}匹".format(sheep=i))