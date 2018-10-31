# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


nat_chisl = input('Друже, введи натуральное число: ')
chet = str()
nechet = str()
for i in nat_chisl:
    if int(i) % 2 == 0:
        chet += i
    else:
        nechet += i
print(f'Введено число {nat_chisl}')
print(f'В {nat_chisl} есть {len(chet)} четных цифр {(chet)}')
print(f'В {nat_chisl} есть {len(nechet)} нечетных цифр {(nechet)}')
