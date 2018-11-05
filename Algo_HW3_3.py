# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

RNG = 10
lst = [random.randint(0, RNG * RNG) for i in range(RNG * 2)]
# Второй сделанный рабочий вариант.
# Быстрее первого варианта (описан в само низу), однако имеет слабое место.
# При повторяющихся min и max, меняет только одну пару значений, а не все.
mx_nb = mn_nb = 0
for j in range(len(lst)):
    if lst[j] >= lst[mx_nb]:
        mx_nb = j
    elif lst[j] <= lst[mn_nb]:
        mn_nb = j
print(f'Максимальное значение: {lst[mx_nb]}. Минимальное значени: {lst[mn_nb]}')
print(f'Изначальный список: {lst}')
lst[mx_nb], lst[mn_nb] = lst[mn_nb], lst[mx_nb]
print(f'Заменный список:    {lst}')


# Первый сделанный рабочий вариант.
# Данный вариант работает на все повторяющиеся элементы min и max.
# При этом он более ресурсоемкий, чем второй вариант.
# mx = mn = lst[0]
# for j in lst:
#     if j >= mx:
#         mx = j
#     elif j <= mn:
#         mn = j
# print(f'Максимальное значение: {mx}. Минимальное значени: {mn}')
# print(f'Изначальный список: {lst}')
# for i in range(len(lst)):
#     if mx == lst[i]:
#         lst[i] = mn
#     elif mn == lst[i]:
#         lst[i] = mx
# print(f'Заменный список:    {lst}')