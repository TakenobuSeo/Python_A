#素因数分解を行うプログラム

# import sys
# args = sys.argv

# divided_num = int(args[1])



#デバッグ用
divided_num = 2023
# 素因数分解の結果を格納する配列
output_list = []

# 割られる数が１になるまでループ
while divided_num != 1:

# 2から割られる数自体までループ
# divided_num + 1しないと割られる数自体で割ってくれない
    for div_num in range(2,divided_num+1):
        #割り切れたら（約数ならば）
        if divided_num % div_num == 0:
            #約数を配列に保存
            output_list.append(div_num)
            #解がfloatになるのでintに変換
            divided_num = int(divided_num/div_num)
            break #forを抜ける
            
#解の出力
print(output_list, end="")




