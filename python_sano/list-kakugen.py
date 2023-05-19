import random

not_kakugen = [
    "本田とじゃんけんしよう！",
    "俺の勝ち！",
    "なんで負けたか明日まで考えといてくださいね"
]

i = random.randint(0,len(not_kakugen)-1)

print(not_kakugen[i])