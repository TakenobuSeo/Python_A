import sys
import func_salary

args = sys.argv



for i in range(1, len(args)):
    r_salary = func_salary.calc_salary(int(args[i]))
    print("給与:", int(args[i]), "支給額:", r_salary[0], "税額:",r_salary[1]) 