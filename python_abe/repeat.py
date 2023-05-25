import sys
args = sys.argv
n = int(args[1])
num = 0
while True:
    num = num+n
    if num == 100:
        print("Just 100!")
        break
    elif(num>100):
        print("Over!")
        break