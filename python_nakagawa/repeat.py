import sys
args = sys.argv

num = int(args[1])
sum = 0
while sum <= 100 :
    if sum == 100:
        print("Just 100!", end="")
        break
    sum += num

else:
    print("Over!", end="")
