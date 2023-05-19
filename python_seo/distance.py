import sys
args = sys.argv

# 引数を数値型に変換
sta1 = args[1]
sta2 = args[2]

stations = {
    "東京":0.00, "品川":6.78, "新横浜":25.54, 
    "名古屋":342.02, "京都":476.31, "新大阪":515.35}

long1 = stations[sta1]
long2 = stations[sta2]

long = [long1, long2]

long = sorted(long, reverse=True)
distance = long[0] - long[1]

print(distance)