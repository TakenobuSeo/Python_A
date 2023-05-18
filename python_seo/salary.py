import sys
import math

args = sys.argv

# 
salary = int(args[1])
if salary <= 1000000:
    tax = salary * 0.1
else:
    tax1 = 1000000 * 0.1
    tax2 = (salary - 1000000) * 0.2
    tax = tax1 + tax2

tax = math.floor(tax)

supply = salary - tax

print("支給額:{supply}、税額:{tax}".format(supply=supply, tax=tax), end="")