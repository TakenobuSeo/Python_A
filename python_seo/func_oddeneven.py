import sys
args = sys.argv

#関数を定義
def calcvalue(*nums):
    #あまりを算出
    for num in nums:

        mod = num % 2

        #あまりの値から奇数偶数判定
        if mod != 0:
            print(str(num) + "は奇数")
        else:
            print(str(num) + "は偶数")

calcvalue(int(args[1]), int(args[2]), int(args[3]))