# モジュールをインポート
import sys, func_salary
args = sys.argv

#　関数を変数に格納する
calcsalary = func_salary.calcsalary

#　iの初期値を１にする
for i in range(1,len(args)):
    salary = int(args[i])
    # 関数の返り値２つを２つの変数に格納
    payment, tax_amount = calcsalary(salary)
    print(f'給与:{salary}、支給額:{payment}、税額:{tax_amount}')