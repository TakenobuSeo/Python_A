import sys
args = sys.argv

num = int(args[1])

# 2で割った余りが0で偶数、それ以外は奇数
if num % 2 == 0:
    print("偶数", end="")
else:
    print("奇数", end="")