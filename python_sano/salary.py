import sys
import math

args = sys.argv
pay_amount = int(args[1])

# 100万円を超えた分は20%, 超えない分は10%の課税
if pay_amount >= 100 * 10000:
    tax = (pay_amount - 100 * 10000) * 0.20 + 100 * 10000 * 0.10
else:
    tax = pay_amount * 0.10

# 税額は小数第一位を四捨五入し、整数とする
tax = math.floor(tax)
salary = pay_amount - tax

print(f"支給額:{salary}、税額:{tax}", end="")
