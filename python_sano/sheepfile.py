import sys
import os

args = sys.argv
sheep_num = int(args[1])
path = os.path.join("..", "files", "sheep.txt")

if os.path.exists(path):
    with open(path, mode="r+") as f:
        past_str = f.read()

        f.write("\n")

        count = past_str.count("回目")+1
        f.write(f"<{count}回目処理後>\n")

        for i in range(1, sheep_num+1):
            f.write(f"ひつじが{i}匹\n")
            
else:
    with open(path, mode="x") as f:
        f.write("<1回目処理後>\n")
        for i in range(1, sheep_num+1):
            f.write(f"ひつじが{i}匹\n")

