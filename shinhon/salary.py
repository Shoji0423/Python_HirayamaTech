# salaryに給料の金額を代入
import sys
salary = int(sys.argv[1])

# 税額を算出
tax = 0
if salary > 1000000:
    tax = round((salary-1000000)*0.2 + 1000000*0.1)
else:
    tax = round(salary*0.1)

# 結果を出力
output = "支給額:{0}、税額:{1}".format(salary-tax, tax)
print(output)

# ノート
# from decimal import Decimal, ROUND_HALF_UP
# decs = "支給額:{0}、税額:{1}".format(Decimal(str(salary)).quantize(Decimal("0"), rounding=ROUND_HALF_UP), Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP))
# print(tax)
# print(Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP))