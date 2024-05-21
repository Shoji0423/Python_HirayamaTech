import sys
from project_database import func_aquacalc as aqu

input = sys.argv
date = str(input[1])
adult = int(input[2])
child = int(input[3])

print(aqu.calc_aquaSum(date, adult, child))