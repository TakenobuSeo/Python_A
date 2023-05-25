# 支払額 payment
# 給与額 salary
# 税額 tax
# 税率 tax_rate
import func_salary
import sys
import math
args = sys.argv
salaries = args
for i,salary in enumerate(salaries):
    if i == 0:
        continue
    payment,tax = func_salary.calc_salary(salary)
    print(f'支給額:{math.floor(payment)}、税額:{math.floor(tax)}',end="")