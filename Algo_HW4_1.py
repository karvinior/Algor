# 3_3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import timeit
import cProfile
import random

# Вариант с заменой одной пары max и min

def one_pair(rng):
    lst = [random.randint(-rng//2, rng//2) for _ in range(rng**2)]
    mx_nb = mn_nb = 0
    for j in range(len(lst)):
        if lst[j] >= lst[mx_nb]:
            mx_nb = j
        elif lst[j] <= lst[mn_nb]:
            mn_nb = j
    lst[mx_nb], lst[mn_nb] = lst[mn_nb], lst[mx_nb]
    return lst

# python -m timeit -n 100 -s "import Algo_HW4_1" "Algo_HW4_1.one_pair(10)"
# "Algo_HW4_1.one_pair(10)"
# 100 loops, best of 5: 117 usec per loop
# "Algo_HW4_1.one_pair(100)"
# 100 loops, best of 5: 11.9 msec per loop
# "Algo_HW4_1.one_pair(200)"
# 100 loops, best of 5: 47.8 msec per loop

# cProfile.run("one_pair(200)")  1    0.004    0.004    0.072    0.072 Algo_HW4_1.py:9(one_pair)
# cProfile.run("one_pair(100)")  1    0.001    0.001    0.018    0.018 Algo_HW4_1.py:9(one_pair)
# cProfile.run("one_pair(10)")   1    0.000    0.000    0.000    0.000 Algo_HW4_1.py:9(one_pair)

# Вариант, меняющий местами все max и min

def all_pair(rng):
    lst = [random.randint(-rng//2, rng//2) for _ in range(rng**2)]
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
    return lst

# python -m timeit -n 100 -s "import Algo_HW4_1" "Algo_HW4_1.all_pair(10)"
# "Algo_HW4_1.all_pair(10)"
# 100 loops, best of 5: 118 usec per loop
# "Algo_HW4_1.all_pair(100)"
# 100 loops, best of 5: 12 msec per loop
# "Algo_HW4_1.all_pair(200)"
# 100 loops, best of 5: 48.5 msec per loop

# cProfile.run("all_pair(200)")  1    0.005    0.005    0.073    0.073 Algo_HW4_1.py:33(all_pair)
# cProfile.run("all_pair(100)")  1    0.001    0.001    0.018    0.018 Algo_HW4_1.py:33(all_pair)
# cProfile.run("all_pair(10)")   1    0.000    0.000    0.000    0.000 Algo_HW4_1.py:33(all_pair)


# Вывод: Алгоритм с заменой всех переменных на сотые доли медленнее алгоритма
# с заменой только одной пары