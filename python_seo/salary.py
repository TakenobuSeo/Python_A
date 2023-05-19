import sys
import math

args = sys.argv

# 100万以下は10%、100万以上は100万と、残りを分けて税額計算
salary = int(args[1])
if salary <= 1000000:
    tax = salary * 0.1
else:
    tax1 = 1000000 * 0.1
    tax2 = (salary - 1000000) * 0.2
    tax = tax1 + tax2

# mathを使って四捨五入、税額を計算
tax = math.floor(tax)

# 支給額を計算(給与-税額)
supply = salary - tax

print("支給額:{supply}、税額:{tax}".format(supply=supply, tax=tax), end="")