import sys

args = sys.argv

# 引数を数値型に変換
sta1 = args[1]
sta2 = args[2]

# リストを作成
stations = {
    "東京":0.00, "品川":6.78, "新横浜":25.54, 
    "名古屋":342.02, "京都":476.31, "新大阪":515.35}

# 引数の2つを変数に代入
long1 = stations[sta1]
long2 = stations[sta2]

# 2つの引数をlongリストに代入
long = [long1, long2]

# longを降順で並び替えて、少数点第3位以下を四捨五入
long = sorted(long, reverse=True)
distance = round(long[0] - long[1], 2)

print(distance, end="")