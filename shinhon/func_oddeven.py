# inputに引数を代入したあと、数値をnum_listにまとめる
import sys
input = sys.argv
num_list = list(map(int, input[1:]))

# 数値を判断するための関数
def oddeven_checker(num):
    '''引数は奇数と偶数かを判断する'''
    if num % 2:
        print(f'{num}は奇数')
    else:
        print(f'{num}は偶数')

# リストの中にある数値の判断結果を出力
for i in num_list:
    oddeven_checker(i)