def calcsalary(salary):
    from decimal import Decimal, ROUND_HALF_UP

#税額の計算
    if salary > 1000000:
        tax = (salary-1000000) * 0.2 + 100000
    elif salary <= 1000000:
        tax = salary * 0.1
#四捨五入の計算
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
#支給額の計算
    pay_amount = salary - tax
#表示
    print("支給額:{0}、税額:{1}".format(pay_amount, tax),end="")