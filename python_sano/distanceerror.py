import sys 
import math

args = sys.argv
measuring_section = [args[1], args[2]]

distance_dict ={
    "東京"      : 0.00,
    "品川"      : 6.78,
    "新横浜"    : 25.54,
    "名古屋"    : 342.02,
    "京都"      : 476.31,
    "新大阪"    : 515.35  
}

try:
    distance = abs(distance_dict[measuring_section[0]] - distance_dict[measuring_section[1]])
    result = round(distance, 2)
    print(result , end="")
    
except:
    print("のぞみの停車駅を引数に設定してください", end="")