import sys

num = int(sys.argv[1])

primeHolder = []

# 2で割れる素因数を洗い出す
while num % 2 == 0:
    primeHolder.append(2)
    num //= 2 #小数点はいらない

# 奇数の素因数を洗い出す
t = 3
while t * t <= num:
    if num % t == 0:
        primeHolder.append(t)
        num //= t
    else:
        t += 2

# numは1ではない場合は素数なので、リストに追加
if num != 1:
    primeHolder.append(num)

print (primeHolder)