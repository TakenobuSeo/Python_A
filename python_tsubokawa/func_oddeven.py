
from func import func as calcFunc

# calcFunc = func
#debug
# num1 = 2
# num2 = 3
# num3 = 4

#入力値の取得
import sys
args = sys.argv
# num1 = int(args[1])
# num2 = int(args[2])
# num3 = int(args[3])
print(len(args))
#forで回すことで引数の数に関係なく処理
for i in range(1, len(args)):
    print(args[i])
    calcFunc.calcvalue(int(args[i]))

# calcFunc.calcvalue(num1)
# calcFunc.calcvalue(num2)
# calcFunc.calcvalue(num3)


