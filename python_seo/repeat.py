import sys
args = sys.argv

# 引数を数値型に変換
num = int(args[1])

# 初期値を合計の関数に代入
sum = num

# 合計が100、100以上、100以下で条件分岐。
# 合計が100未満であれば、合計値に引数を足す。
while True:
    if sum == 100:
        print("Just 100!")
        break

    elif sum > 100:
        print("Over!")
        break

    else:
     sum += num