# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.

# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках.

import random

m = int(input('Введи коэффициент "m" для генерации массива размером 2m + 1: '))
left_side = 0
right_side = 0

rnd = [random.randint(0, 99) for i in range(2*m + 1)]     # randint(a, b) return a random integer N such that a <= N <= b
print(rnd)

for i in rnd:
    for j in rnd:
        if j > i:
            left_side += 1
        elif j < i:
            right_side += 1
    if right_side == left_side:
        print(f'Медиана: {i}')
        break
    else:
        left_side = 0
        right_side = 0