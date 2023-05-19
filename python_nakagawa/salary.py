import sys
from decimal import Decimal, ROUND_HALF_UP

args = sys.argv
salary = int(args[1])

#給与が1,000,000万以上であれば、超えた分は税率が20％
if salary > 1000000:
    over = salary - 1000000
    tax =  over * 0.2 + 100000
else:
    tax = salary * 0.1

tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
pay = salary - tax
print(f'支給額:{pay}、税額:{tax}', end="")
