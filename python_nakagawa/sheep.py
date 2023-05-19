#ひつじを数える
import sys
args = sys.argv

# sheep_sum = int(args[1])
sheep_sum = [1,2,3,4]

#渡されたひつじの数だけ繰り返す
for i in range(len(sheep_sum)):
    print(f'ひつじが{i + 1}匹')