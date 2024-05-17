from func_salary import calcsalary as calc
import sys
args=sys.argv
salay=[]
salay.append(int(args[1]))
salay.append(int(args[2]))
salay.append(int(args[3]))
for i in range(3):
    tax=calc(salay[i])
    print("給与:{0}、支給額:{1}、税額:{2}".format(salay[i],salay[i]-tax, tax))