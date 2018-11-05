# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних # элементов
# строк. Программа должна вычислять сумму введенных элементов # каждой строки
# и записывать ее в ее последнюю ячейку. В конце следует вывести полученную матрицу.

mtrx = [[0] * 5 for _ in range(4)]
spam_last_elem = 0

for n in range(len(mtrx)):
    for m in range(len(mtrx)):
        mtrx[n][m] = int(input(f'Neo, давай введем {m+1}-й элемент матрицы {n+1}: '))
        spam_last_elem += mtrx[n][m]
    mtrx[n][m+1] = spam_last_elem
    spam_last_elem = 0
print(mtrx)