import sys
args = sys.argv
from decimal import Decimal, ROUND_HALF_UP

departureSt = args[1]
arrivalSt = args[2]

#東京駅からの距離
distanceData = {
    "東京": 0.00,
    "品川": 6.78,
    "新横浜": 25.54,
    "名古屋": 342.02,
    "京都": 476.31,
    "新大阪": 515.35
}

try:
    #出発駅と到着駅の距離
    distance = distanceData[arrivalSt] - distanceData[departureSt]
    #結果を絶対値＆四捨五入
    result = Decimal(str(abs(distance))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    print(result, end="")
except:
    #入力エラーが起きた場合
    print("のぞみの停車駅を引数に設定してください", end="")
