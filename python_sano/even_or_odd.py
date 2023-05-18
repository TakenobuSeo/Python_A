import sys

args = sys.argv
number = int(args[1])

if number%2 == 1:
    print("奇数", end="")
else:
    print("偶数", end="")
