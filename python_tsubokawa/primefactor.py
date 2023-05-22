# import sys
# args = sys.argv

# num = int(args[1])


input_num = 8
# 素因数分解の結果を格納する配列
output_list = []

for i in range(2,input_num):
    if input_num % i == 0: #割り切れるとき
        output_list.append(i)
        input_num = input_num / i
        print(input_num)
        # for j in range(2, devided_num):
        #     if devided_num % j == 0:
        #         output_list.append(j)
        #         dev
        # div_num = num / i
        # if(div_num==num):
        #     output_list.append(i)
print(output_list)

# start_num = 2
# while(start_num<num):
