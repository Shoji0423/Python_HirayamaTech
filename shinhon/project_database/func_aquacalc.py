import datetime

import os, sys
sys.path.append(os.path.dirname(__file__)) #相対パスを指定する

from database import session
from tables import Holiday

# 平日と土日の料金
tickets_weekend = {
    "大人": 2400,
    "子供": 1500
}

tickets_normal = {
    "大人": 2000,
    "子供": 1200
}

def output_date(str_date):
    '''日付を出力する'''
    return datetime.date(int(str_date[:4]), int(str_date[4:6]), int(str_date[6:]))

def calc_aquaPrice(date_list, adult, child):
    '''合計金額を出す'''
    return date_list["大人"] * adult + date_list["子供"] * child

def calc_aquaSum(input_date, adult, child):
    '''平日か祝日の金額を出力する'''
    dt = output_date(input_date)

    select_holiday = session.query(Holiday).filter(Holiday.holi_date == dt)

    if (int(dt.strftime('%w')) == 0 or int(dt.strftime('%w')) == 6) or select_holiday.count() != 0:
        output = calc_aquaPrice(tickets_weekend, adult, child)
        return output
    else:
        output = calc_aquaPrice(tickets_normal, adult, child)
        return output