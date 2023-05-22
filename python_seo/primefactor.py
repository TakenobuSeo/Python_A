import sys
args = sys.argv

# 引数を数値型に変換
num = int(args[1])

sosu = []

for i in range(2, num+1):
    while num % i == 0:
        sosu.append(i)
        print(i)
        num = num // i

print(sosu)