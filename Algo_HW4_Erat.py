# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена. Второй - без
# использования "решета". Проанализировать скорость и сложность алгоритмов.

import timeit
import cProfile

def no_reshet_erat(n):
    simp_nbr_lst = [2, 3, 5, 7]   # список первых 4-х простых чисел, для поиска остальных
    dict = {}   # cловарь для записи простых чисел и их номеров, начиная с 5-ого числа
    spam = 4    # переменная для временного учета находимых номеров простых чисел
    distnc = 10 # переменная для формирования отрезков поиска простых чисел
    while True:
        if n <= 4:    # если простое число с номером до 4-х включительно
            for i in range(len(simp_nbr_lst)):
                if i == n:
                    return simp_nbr_lst[n]
        else:         # для простых числе с номерами начиная с 5-го
            for j in range(distnc, distnc+100):
                for m in simp_nbr_lst:    # цикл для перебора однознаковых простых чисел с целью деления на них
                    if j % m == 0:
                        break      # прерывание цикла еребора однознаковых простых чисел, если число j не простое
                else:  # если найдено простое число
                    spam += 1
                    dict[spam] = j
                if n == spam:     # если совпал искомый номер и номер найденного простого числа
                    return dict[n]
            distnc += 100

# python -m timeit -n 100 -s "import Algo_HW4_Erat" "Algo_HW4_Erat.no_reshet_erat(10)"
# "Algo_HW4_Erat.no_reshet_erat(10)"
# 100 loops, best of 5: 3.99 usec per loop
# "Algo_HW4_Erat.no_reshet_erat(100)"
# 100 loops, best of 5: 72.2 usec per loop       # Вывод - код не оптимальный :*(
# "Algo_HW4_Erat.no_reshet_erat(1000)"
# 100 loops, best of 5: 799 usec per loop

# cProfile.run('no_reshet_erat(1000000)') 1    0.863    0.863    0.863    0.863 Algo_HW4_Erat.py:8(no_reshet_erat)
# cProfile.run('no_reshet_erat(100000)')  1    0.090    0.090    0.090    0.090 Algo_HW4_Erat.py:8(no_reshet_erat)
# cProfile.run('no_reshet_erat(10000)')   1    0.009    0.009    0.009    0.009 Algo_HW4_Erat.py:8(no_reshet_erat)



def reshet_erat(x):
    simp_lst = [0, 0, 2, 0, 3, 0, 5, 0, 7]     
    count = 4       # начало счетчика элементов, с учетом уже проставленных однозначных простых чисел
    n = 9           # стартовая переменная для формирования списка элементов с целью поиска простых чисел
    while True:
        if x <= 4:  # Случай выбора номера однозначного простого числа
            if x == 1:
                return 2
            elif x == 2:
                return 3
            elif x == 3:
                return 5
            elif x == 4:
                return 7
            break
        for i in range(n, n + 100):     # доформирвание массива
            simp_lst.append(i)
        for y in simp_lst:
            for z in range(n, n + 100): # цикл для онуления непростых чисел
                if y != 0:
                    if simp_lst[z] % y == 0 and simp_lst[z] != y:
                        simp_lst[z] = 0
        for j in range(n, n + 100):     # цикл для вычисления номеров простых чисел
            if simp_lst[j] != 0:
                count += 1
            if count == x:
                return simp_lst[j]
        n += 100                        # прирост счетчика для формирования нового диапазона

# Дописывал функцию def reshet_erat(x) сидя на работе. Python тут нет :**(((
# Смог протестировать только через в онлайн эмуляторе, т.е. без коммандной строки. Прошу понять и простить.



# print(timeit.timeit("reshet_erat(10)", setup="from __main__ import reshet_erat", number=100))
# 0.11305285900016315
# print(timeit.timeit("reshet_erat(100)", setup="from __main__ import reshet_erat", number=100))
# 2.9730736300116405
# print(timeit.timeit("reshet_erat(50)", setup="from __main__ import reshet_erat", number=100))
# 0.7532408970000688


# cProfile.run('reshet_erat(100)')  1    0.027    0.027    0.027    0.027 main.py:44(reshet_erat)
# cProfile.run('reshet_erat(10)')   1    0.001    0.001    0.001    0.001 main.py:44(reshet_erat)
# cProfile.run('reshet_erat(1000)') 1    4.483    4.483    4.484    4.484 main.py:44(reshet_erat)  