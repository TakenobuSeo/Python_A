import sys
import os
args = sys.argv
n = int(args[1])
path = 'files/sheep.txt'
is_file = os.path.isfile(path)

for i in range(n):
    f = open(path, 'w')
    f.write(f'ひつじが{i}匹')
    f.close()