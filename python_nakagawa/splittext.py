import sys
args = sys.argv

#指定したn番目の単語を出力する

#英文
text = args[1]
#n番目
num = int(args[2])

#英文をスペースで区切ってリストにする
list = text.split(" ")
print(list[num - 1], end="")