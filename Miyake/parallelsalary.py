import func_salary
import sys
args = sys.argv

#引数を変数に代入
salary1 = int(args[1])
salary2 = int(args[2])
salary3 = int(args[3])

#salary = [int(args[1]), int(args[2]), int(args[3])]

for i in [salary1, salary2, salary3]:
#print(func_salary.calcsalary(salary))
    func_salary.calcsalary(i)