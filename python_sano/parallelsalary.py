import sys
import func_salary

args = sys.argv

for pay_amount in  map(int,args[1:]):
    salary, tax = func_salary.get_salary_tax(pay_amount)
    print(f"給与：{pay_amount}、支給額：{salary}、税額：{tax}") 