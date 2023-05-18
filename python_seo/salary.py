import sys
from decimal import Decimal, ROUND_HALF_UP
args = sys.argv

salary = int(args[1])
if salary <= 1000000:
    tax = salary * 0.1
else:
    tax1 = 1000000 * 0.1
    tax2 = (salary - 1000000) * 0.2
    tax = tax1 + tax2

tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)

supply = salary - tax

print("支給額:{supply}、税額:{tax}".format(supply=supply, tax=tax), end="")