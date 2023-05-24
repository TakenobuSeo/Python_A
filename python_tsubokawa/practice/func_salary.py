import math

def calcsalary(salary):
    payment = 0
    tax_amount = 0
    if salary >= 100 * 10000:
        tax_amount = math.floor((salary - 100 * 10000)* 0.2 + 100 * 10000 * 0.1)
    else:
        tax_amount = math.floor(salary * 0.1)
    payment = salary - tax_amount
    return payment, tax_amount