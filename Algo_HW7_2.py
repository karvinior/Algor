# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

def merge_sort(left, right):                        # эта красавица деляет сортировку и слияние
    index_left = 0
    index_right = 0
    spam_lst = []
    while True:
        if index_left == len(left) and index_right == len(right):    # выход из цикла
            break
        elif index_right == len(right):                              # лекарство на случай неравной right и left части
            spam_lst.append(left[index_left])
            index_left += 1
        elif index_left == len(left):                                # тоже лекарство как в стр 13
            spam_lst.append(right[index_right])
            index_right += 1
        elif left[index_left] <= right[index_right]:
            spam_lst.append(left[index_left])
            index_left += 1
        elif left[index_left] >= right[index_right]:
            spam_lst.append(right[index_right])
            index_right += 1

    return spam_lst


def split_merge_all(lst):                           # эта красотка делит список пополам и вызывает рекурсию +
    if len(lst) == 0 or len(lst) == 1:              # возврат результата при "атомарном" уровне списка.
        return lst
    else:                                           # деление списка до атамарного уровня +
                                                    # возврат результа на уровне выше "атамарного"
        middle = len(lst) // 2
        left_side = split_merge_all(lst[:middle])
        right_side = split_merge_all(lst[middle:])
        return merge_sort(left_side, right_side)

rnd = [random.randint(0, 49) for i in range(10)]     # randint(a, b) return a random integer N such that a <= N <= b

print(rnd)
print(split_merge_all(rnd))