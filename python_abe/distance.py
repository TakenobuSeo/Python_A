st_dict = {"東京": 0.00, "品川": 6.78,"新横浜":25.54,"名古屋":342.02,"京都":476.31,"新大阪":515.35} 
import sys
args = sys.argv
go_dis = st_dict[args[1]]
to_dis = st_dict[args[2]]
print(round(abs(go_dis - to_dis),2),end="")