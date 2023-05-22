# デバッグ用
# text = 'I am human'
# num = 2 -1

#入力値取得
import sys
args = sys.argv

sentence = args[1]
#指定した番号とインデックス番号が一致するように
num = int(args[2]) - 1

# 半角スペースで単語を区切ってリスト化
word_list = sentence.split()

# 指定された番号の単語を出力
print(word_list[num], end="")