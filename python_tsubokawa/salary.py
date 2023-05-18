import sys
args = sys.argv

#四捨五入のため、モジュールをインポート
from decimal import Decimal, ROUND_HALF_UP

input_salary = int(args[1])
#100万超える部分は20% 
tax_rate_over100 = 0.2

tax_rate_under100 = 0.1


if input_salary > 1000000:
    tax_over100 = (input_salary - 1000000) * tax_rate_over100
    tax_over100 = Decimal(str(tax_over100)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)

    tax_under100 = 1000000 * tax_rate_under100
    tax_under100 = Decimal(str(tax_under100)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)

    tax_amount = tax_over100 + tax_under100
else:
    tax_amount = input_salary * tax_rate_under100
    tax_amount = Decimal(str(tax_amount)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)


provided_salary = input_salary - tax_amount

print('支給額:{}、税額:{}'.format(provided_salary, tax_amount), end="")

