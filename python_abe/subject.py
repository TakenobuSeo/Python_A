import sys
args = sys.argv
math = int(args[1])
jp = int(args[2])
en = int(args[3])
sum = jp + en + math
if ((math >= 70 and jp >= 70 and en >= 70) or sum>=220) and (math >= 50 and jp >=50 and en>=50):
    print('合格',end="")
else:
    print('不合格',end="")