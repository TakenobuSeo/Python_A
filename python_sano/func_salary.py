import math

def get_salary_tax(pay_amount: int) -> list:
    '''給与を渡すと、支給額と税額を戻り値として返す'''
    if pay_amount >= 100 * 10000:
        tax = (pay_amount - 100 * 10000) * 0.20 + 100 * 10000 * 0.10
    else:
        tax = pay_amount * 0.10
    tax = math.floor(tax)
    salary = pay_amount - tax
    return salary, tax