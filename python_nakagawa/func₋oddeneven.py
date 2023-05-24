import sys
args = sys.argv

# 関数を定義
def calcValue(*num):
    for n in num:

        # あまりを算出
        mod = int(n) % 2

        # あまりの値から奇数偶数判定
        if mod != 0:
            print(str(n) + "は奇数")
        else:
            print(str(n) + "は偶数")

# calcValue((int(args[1]), int(args[2]), int(args[3])))

# 引数の数だけ関数を呼び出す。
for i in range(len(args)):
    if i == 0:
        continue
    calcValue(int(args[i]))
