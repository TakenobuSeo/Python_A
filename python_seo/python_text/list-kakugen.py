import random

# リストを作成
kakugen = ["叩き続けなさい。そうすれば開かれます。", "徳は弧ならず。必ず隣あり。", "能ある鷹は爪を隠す", "鬼に金棒", "巧言令色、少なし仁。", "性相近し、習い相遠し。"]

# iにリストの要素数の分のランダム整数を代入
i = random.randrange(0, len(kakugen))

# print(i)
# ランダム整数の要素数の値を出力
print(kakugen[i])