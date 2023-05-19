import sys
args = sys.argv

# 引数をwordsに代入
words = args[1]
# 引数を数値型に変換
num = int(args[2])

# 記号の削除
words = words.replace(".", "")
words = words.replace(",", "")
# words = words.replace("'", "")

# 単語ごとに分け、それをリストにする
words = words.split()

# n番目の単語を出力
word = words[num-1]
print(word)