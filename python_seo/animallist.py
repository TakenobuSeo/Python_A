import sys
args = sys.argv

# 引数を数値型に変換
num = int(args[1])
animal = args[2]

# animals配列を定義
animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

# 第3引数の文字列を第2引数の要素に代入
animals[num] = animal

# animalsの末尾を削除
delete = animals.pop(-1)

# animalsを昇順に並び替え
animals = sorted(animals)

print(animals)
