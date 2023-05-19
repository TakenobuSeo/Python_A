import sys

# args[1]:素因数分解する整数
args = sys.argv
num = int(args[1])

# 素因数分解して、素因数をprime_factorに格納していく
prime_factor = []
while num > 1:
    for i in range(2, num+1):
        if num % i == 0:
            num /= i
            num = int(num)
            prime_factor.append(i)
            break

print(prime_factor, end="")