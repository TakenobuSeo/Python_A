import sys
args = sys.argv

#ORIGINAL
num = int(args[1])
sum = 0
# while sum <= 100 :
#     if sum == 100:
#         print("Just 100!", end="")
#         break
#     sum += num

# else:
#     print("Over!", end="")

#可読性UP
while True:
    if sum == 100:
        print("Just 100!", end="")
        break
    elif sum > 100:
        print("Over!", end="")
        break
    else:
        sum += num
