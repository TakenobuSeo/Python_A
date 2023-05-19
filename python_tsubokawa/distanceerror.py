distance_from_Tokyo = {
    '東京':0.00,
    '品川':6.78,
    '新横浜':25.54,
    '名古屋':342.02,
    '京都':476.31,
    '新大阪':515.35}


#デバッグ用
# departure_station = '新大阪'
# arrival_station = '東京'

#入力値取得
import sys
args = sys.argv

#入力値を出発駅、到着駅に代入
departure_station = args[1]
arrival_station = args[2]
try:
#距離を辞書から選択
    departure_distance = distance_from_Tokyo[departure_station]
    arrival_distance = distance_from_Tokyo[arrival_station]

    #2駅間の距離を計算
    #負の場合でも良いように絶対値計算
    distance_between = abs(arrival_distance - departure_distance)

    #少数2桁で丸めて出力
    print(round(distance_between,2), end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="")
