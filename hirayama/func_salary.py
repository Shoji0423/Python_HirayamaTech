from decimal import Decimal,ROUND_HALF_UP

def calcsalary(salay):
    if salay <= 1000000 :
        tax=salay*0.1
    else:
        over=salay-1000000
        tax=over*0.2
        tax=tax+1000000*0.1   
    tax=Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    return tax