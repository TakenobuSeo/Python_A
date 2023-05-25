#ひつじを数える
import sys
args = sys.argv

# sheep_sum = int(args[1])
sheep_sum = int(args[1])

with open("sheep.txt", mode="w", encoding="utf-8") as f:
    #渡されたひつじの数だけ繰り返す
    for i in range(sheep_sum):
     f.write(f'ひつじが{i + 1}匹です\n')