# 支払額 payment
# 給与額 salary
# 税額 tax
# 税率 tax_rate
import sys
import math

def calc_salary(salary):
    tax_rate = 0
    salary = int(salary)
    if (salary < 1000000):
        tax_rate = 0.1
        tax = salary*tax_rate
        payment = salary - tax
        return payment,tax
    else:
        tax_rate = 0.1
        tmp = salary - 1000000
        tax = 1000000 * tax_rate
        tax = tax + tmp * 0.2
        payment = salary - tax
        return payment,tax