import sys
args = sys.argv

math = int(args[1])
jap = int(args[2])
eng = int(args[3])

sum = math + jap + eng
if (math>=70 and jap>=70 and eng>=70) or (sum>=220):
    if not(math<50 or jap<50 or eng<50):
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")