import sys

# 引数の読み取り
args = sys.argv
add_index = int(args[1])
add_animal_name = args[2]

animal_list =   ["giraffe", "tiger", "zebra", "elephant", "lion"]

# 第2引数で設定した要素の位置に、第3引数の動物名を挿入する
animal_list.insert(add_index, add_animal_name)

animal_list.pop()

# 昇順でソート
animal_list.sort()

print(animal_list, end="")