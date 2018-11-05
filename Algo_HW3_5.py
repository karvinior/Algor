# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

RNG = 10

rng = [random.randint(-RNG*RNG, RNG*RNG) for _ in range(RNG*2)]
mx_ng = -RNG*RNG    # переменная для учета максимального отрицательного элемента
pos_mx_ng = 0       # переменная для учета позиции макс.отриц.элемента
print(rng)

for i in range(len(rng)):
    if rng[i] < 0 and rng[i] > mx_ng:
        mx_ng = rng[i]
        pos_mx_ng = i
print(f'Максимальный отрицательный элемент {mx_ng} '
      f'занимает позицию {pos_mx_ng} если начинать считать с нуля.')