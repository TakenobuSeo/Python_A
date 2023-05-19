import sys

args = sys.argv

# 引数の値を足し続けて100になるか100を超えたら出力して終了
num = int(args[1])
sum = 0
while True:
    sum += int(num)
    if sum == 100:
        print("Just 100!", end="")
        break
    elif sum > 100:
        print("Over!", end="")
        break
