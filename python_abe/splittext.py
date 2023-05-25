import sys
args = sys.argv
text = args[1]
texts = text.split(' ')
num = int(args[2])
print(texts[num-1],end="")