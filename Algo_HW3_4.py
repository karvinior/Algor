# 4. Определить, какое число в массиве встречается чаще всего.

import random

RNG = 10
cnt = 1
mx_cnt = 0
mx_nbr = 0

lst = [random.randint(0, RNG) for _ in range(RNG)]
for i in range(len(lst)):
    for j in range(1+i, len(lst)):
        if lst[j] == lst[i]:
            cnt += 1
    if cnt > mx_cnt:
        mx_cnt = cnt
        mx_nbr = lst[i]
    cnt = 1
print(f'Вот список, не пугайся: {lst}')
print(f'Наибольшее количество раз {mx_cnt} встречается элемент {mx_nbr}')