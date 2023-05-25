import sys
args = sys.argv

num = int(args[1])

numList = []
#与えられた値を素因数分解
while num > 1:
  for i in range(2, int(num) +1):
      if num % i == 0:
          num /= i
          numList.append(i)
          break

print(numList, end="")