import sys

# args[1]：半角スペースで区切られた文字列
# args[2]：取り出したい単語が何番目か
args = sys.argv
text = args[1].split(" ")
index = int(args[2])-1

print(text[index], end="")