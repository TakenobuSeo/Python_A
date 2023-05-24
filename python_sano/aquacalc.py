import sys
from datetime import datetime

args = sys.argv
dt = datetime.strptime(args[1], "%Y%m%d")
count_adult = int(args[2])
count_child = int(args[3])

# 土日と平日で値段を変える
if dt.strftime("%a") in ["Sat", "Sun"]:
    price_adult = 2400
    price_child = 1500
else:
    price_adult = 2000
    price_child = 1200

total_price = price_adult * count_adult + price_child * count_child

print(total_price, end="")
