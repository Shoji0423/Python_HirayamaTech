def calc_salary(salary):
    # 税額を算出
    tax = 0
    if salary > 1000000:
        tax = round((salary-1000000)*0.2 + 1000000*0.1)
    else:
        tax = round(salary*0.1)

    # 結果を出力
    return f"給与:{salary}、支給額:{salary-tax}、税額:{tax}"