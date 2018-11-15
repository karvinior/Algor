# 3_3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import timeit
import cProfile
import random
import sys


# 1. Вариант с заменой одной пары max и min

def one_pair(rng):
    lst = [random.randint(-rng // 2, rng // 2) for _ in range(rng ** 2)]
    mx_nb = mn_nb = 0
    for j in range(len(lst)):
        if lst[j] >= lst[mx_nb]:
            mx_nb = j
        elif lst[j] <= lst[mn_nb]:
            mn_nb = j
    lst[mx_nb], lst[mn_nb] = lst[mn_nb], lst[mx_nb]
    return rng, lst[mn_nb], lst[mx_nb], j, lst              # Функция возвращает переменные, которые будем измерять
                                                            # Через locals() объем получается меньше и неправильный.

# 2. Вариант, меняющий местами все max и min

def all_pair(rng):
    lst = [random.randint(-rng // 2, rng // 2) for _ in range(rng ** 2)]
    mx = mn = lst[0]
    for j in lst:
        if j >= mx:
            mx = j
        elif j <= mn:
            mn = j
    for i in range(len(lst)):
        if mx == lst[i]:
            lst[i] = mn
        elif mn == lst[i]:
            lst[i] = mx
    return rng, mn, mx, i, j, lst                           # Аналогично описанной выше ситации :(


def size(x, size_sum_):                                     # На входе return из одной функци выше
                                                            # + пустой список для учета объема переменных
    size_sum_.append(sys.getsizeof(x))                      # Формирую список с рамерами перменных.
                                                            # Вариант с простым суммированием не смог реализовать :*(
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size(key, size_sum_)
                size(value, size_sum_)
        elif not isinstance(x, str):
            for i in x:
                size(i, size_sum_)
    return sum(size_sum_)                                   # возвращает сумму объема переменных функции 1. или 2.
                                                            # + веса массива для учета объема размера переменных

N = 10
print(f'Памяти выделено под 1. вариант {size(one_pair(N), []) + sys.getsizeof(N)}')
print(f'Памяти выделено под 2. вариант {size(all_pair(N), []) + sys.getsizeof(N)}')

# Для данного случая N = 100 (или списки из 10 000 элементов) выделено памяти:
# под 1. вариант 367480 байт
# под 2. вариант 367504 байт