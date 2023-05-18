import sys
args = sys.argv

#3つの整数を足し算しよう
num1 = args[1]
num2 = args[2]
num3 = args[3]

sum = int(num1) + int(num2) + int(num3)

print(sum, end = "")