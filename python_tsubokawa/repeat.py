import sys
args = sys.argv

num = int(args[1])

#デバッグ用
# num = 1

#sumの初期値設定
sum = 0
#sumが100以下の間繰り返し
while sum < 100:
    sum += num
    # print(sum)
    #100になるとwhileを抜ける
    if sum == 100:
        print("Just 100!", end="")
        break
else:
    print('Over!', end="")
    