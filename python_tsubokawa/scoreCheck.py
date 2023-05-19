import sys
args = sys.argv
#数学
score_math = int(args[1])
#国語
score_ja = int(args[2])
#英語
score_en = int(args[3])



total_score = score_math + score_ja + score_en
# print('ok')

if score_math >= 70 and score_ja >= 70 and score_en >= 70:
    if score_math >= 50 and score_ja >= 50 and score_en >=50:
        print('合格', end="")
elif total_score >= 220:
    if score_math >= 50 and score_ja >= 50 and score_en >=50:
        # print('not ok')
        print('合格', end="")
    else:
        print('不合格', end="")
else:
    print('不合格', end="")



