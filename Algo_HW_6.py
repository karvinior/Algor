# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

n = int(input('Введите номер буквы в алфавите: '))
al_number = input(
'''Выберите алфафит:
1 - английский
2 - русский\n'''
                 )
if al_number == '1':
    n = ord('a') + n - 1
elif al_number == '2':
    if n <= 6:
        n = ord('а') + n - 1
    elif n == 7:
        n = 1105
    elif n > 7:
        n = ord('а') + n - 2
        print(n)
print('Это буква', chr(n))