import sys
import func_salary

args = sys.argv

# 引数の数だけcalcsalary()回す
for i in range(len(args)):
    # 引数の一つ目は飛ばす
    if i == 0:
        continue
    # 支給額と税額をもらう
    tax, pay = func_salary.calcSalary(int(args[i]))
    print(f'給与：{args[i]}、 支給額{pay}、税額{tax}')

