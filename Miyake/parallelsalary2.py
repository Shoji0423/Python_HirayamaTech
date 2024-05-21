import func_salary
import sys
args = sys.argv

#引数を変数に代入

salary = [int(args[1]), int(args[2]), int(args[3])]

for i in salary:
#print(func_salary.calcsalary(salary))
    func_salary.calcsalary(i)