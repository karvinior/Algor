# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например,
# если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо
# заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 – если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

def elem_pos(nmbr_type):
    for i in range(len(rng_lst)):
        if rng_lst[i] % 2 == 0:
            lst_even.append(i+1)
        else:
            lst_odd.append(i+1)
    if nmbr_type == '1':
        return lst_even
    elif nmbr_type == '2':
        return lst_odd
    elif nmbr_type == '3':
        return lst_even, lst_odd
    else:
        return None


RNG = 10
rng_lst = [random.randint(0, RNG * RNG) for _ in range(RNG * 2)]
lst_even = []
lst_odd = []

nmbr_type = input('''Что хотимс найти? Нажми:
1 - для поиска чётных цифр
2 - для поиска нечетных цифр
3 - хочешь все и сразу? номера сперва четных, а затем нечетных цифр? ;)
''')

print(f'Вот список: {rng_lst}')
print(f'А вот номера элементов: {elem_pos(nmbr_type)}')