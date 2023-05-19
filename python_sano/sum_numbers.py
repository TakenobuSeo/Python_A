import sys

argv = sys.argv

sum = 0
for a in argv[1:]:
    sum += int(a)

print(sum, end="")