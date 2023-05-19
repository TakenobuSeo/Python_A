import sys
args = sys.argv
num = int(args[1])
flg = True
i = 2
num_array = []
while flg:
    if num == 1:
        break
    if num % i == 0:
        num = num/i
        num_array.append(i)
    else:
        i+=1
print(num_array)