import sys
args = sys.argv
from datetime import datetime

date = args[1]
adultNum = int(args[2])
childNum = int(args[3])

def calcAquariumPrice(date, adultNum, childNum):
    # 日付を曜日に変換
    dt = datetime.strptime(date, "%Y%m%d")
    week = dt.strftime("%a")

    # 土、日は大人2400円、子供1500円
    if week == "Sat" or week == "Sun":
        adultPrice  = 2400
        childPrice = 1500
    else : 
      adultPrice = 2000
      childPrice = 1200

    sum = adultPrice * adultNum + childPrice * childNum
    return sum

sum = calcAquariumPrice(date, adultNum, childNum)
print(sum, end="")