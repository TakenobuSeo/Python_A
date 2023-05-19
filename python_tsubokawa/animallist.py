#  "giraffe", "tiger", "zebra", "elephant", "lion"
animal_list = ['giraffe', 'tiger', 'zebra', 'elephant', 'lion']

# #入力値の取得
# import sys
# args = sys.argv

# index = int(args[1])
# animal = args[2]

#デバッグ用
index = 3
animal = 'human'

#挿入処理
animal_list.insert(index, animal)

print(animal_list, end="")

#削除処理
del animal_list[-1]

print(animal_list, end="")

#ソート処理
animal_list.sort()

print(animal_list, end="")