import sys
args = sys.argv

# 引数を数値型に変換
num = int(args[1])

# num回まで羊を数える
for i in range(1, num + 1):
    print("ひつじが{sheep}匹".format(sheep=i))