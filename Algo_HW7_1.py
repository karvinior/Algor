# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными
# числами на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.

import random

def bubble_sort (lst):
    for x in range(len(lst) - 1):                       # для сортировки пузырьком необходимо
                                                        # на 1 итерациию меньше, чем длина списка
        for i in range(1, len(lst) - x):                # "всплывшие" целые числа не нужно включать в "перебор",
                                                        # соответственно их можно исключить посредством переменной "х",
                                                        # являющейся счетчиком итераций
            if lst[i-1] < lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]
    return lst

rnd = [random.randint(-100, 99) for i in range(10)]     # randint(a, b) return a random integer N such that a <= N <= b

print(rnd)
print(bubble_sort(rnd))