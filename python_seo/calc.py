import sys
args = sys.argv

# 引数を数値型に変換
num1 = int(args[1])
num2 = int(args[2])
num3 = int(args[3])

# ３つの数字の合計
sum = num1 + num2 + num3

print(sum, end="")