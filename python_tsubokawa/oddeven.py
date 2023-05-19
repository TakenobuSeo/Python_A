import sys
args = sys.argv
input_num = int(args[1])
if input_num % 2 == 0:
    print('偶数' ,end="")
else:
    print("奇数", end="")

