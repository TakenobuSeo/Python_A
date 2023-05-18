import sys 
args = sys.argv

math = int(args[1])
japanese = int(args[2])
english = int(args[3])
sum = math + japanese + english

if ((70 <= math <= 100
      and 70 <= japanese <= 100
      and 70 <= english <= 100) 
      or sum >= 220) and (50 <= math ) and (50 <= japanese) and (50 <= english):
    print("合格", end="")
else: 
    print("不合格", end="")