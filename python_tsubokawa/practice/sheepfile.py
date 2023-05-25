import sys
import os
args = sys.argv

num = int(args[1])

path = os.path.join("..","..","..","..","local","day5","text","sheep.txt")

#開始値: 1, 終了値 : 入力値+ 1
# for i in range(1, num+1):
#     # print('ひつじが',i,'匹')
#     with open(path, mode="w") as sf:
#         sf.write(f'ひつじが{i}匹\n')


with open(path, mode="w") as sf:
        for i in range(1,num+1):
            sf.write(f'ひつじが{i}匹\n')
