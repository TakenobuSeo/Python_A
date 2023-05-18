import sys 
args = sys.argv

num = int(args[1])

if num%2 == 0:
    print("偶数", end="")
else:
    print("奇数", end="")