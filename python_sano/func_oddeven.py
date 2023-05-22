import sys
import odd_even
args = sys.argv

for num in args[1:]:
    odd_even.culcvalue(int(num))