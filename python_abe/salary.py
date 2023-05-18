# 支払額 payment
# 給与額 salary
# 税額 tax
# 税率 tax_rate
import sys
import math
args = sys.argv
salary = int(args[1])
tax_rate = 0
if (salary < 1000000):
    tax_rate = 0.1
    tax = salary*tax_rate
    payment = salary - tax
    print(f'支給額:{math.floor(payment)}、税額:{math.floor(tax)}',end="")
else:
    tax_rate = 0.1
    tmp = salary - 1000000
    tax = 1000000 * tax_rate
    tax = tax + tmp * 0.2
    payment = salary - tax
    print(f'支給額:{math.floor(payment)}、税額:{math.floor(tax)}',end="")