import sys

args = sys.argv
scores = [int(args[1]), int(args[2]), int(args[3])]

# 全教科50点以上かつ、（全教科70点以上または、合計220点以上）
if min(scores) >= 50 and ((min(scores) >= 70) or sum(scores) >=220):
    print("合格", end="")
else:
    print("不合格", end="")
