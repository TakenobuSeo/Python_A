import sys
from decimal import Decimal, ROUND_HALF_UP
args = sys.argv

salary = int(args[1])

tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)