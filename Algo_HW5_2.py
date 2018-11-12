# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


def convert_from_0x(x):                                 # функция перевода 16х в 10х число
    x = x[::-1]
    x_summ = 0
    for i in range(len(x)):
        x_summ += dict_0x[x[i]]*(16**i)
    return x_summ

def convert_to_0x(y):                                   # функция для перевода 10х в 16х число
    y_summ = []                                         # не рабоотает для отрицательных и дробных 10-х чисел :(
    while y != 0:
        key = y % 16
        y = y // 16
        y_summ.append(dict_dec[key])
    y_summ = y_summ[::-1]
    return y_summ

dict_0x = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,      # словарь для вызова значений по 16х ключу
           '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'a': 10, 'b': 11, 'c': 12,
           'd': 13, 'e': 14, 'f': 15}

dict_dec = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',     # не смог найти, как вызывать через значение ключ
           5: '5', 6: '6', 7: '7', 8: '8', 9: '9',      # поэтому был вынужден создать второй словарь
           10: 'a', 11: 'b', 12: 'c',
           13: 'd', 14: 'e', 15: 'f'}

nmbr_1 = [str(i).lower() for i in input('Input 1-st number in hexadecimal system: ')]
nmbr_2 = [str(i).lower() for i in input('Input 2-nd number in hexadecimal system: ')]

dst = input('Choose your destiny. Press numeral: \n'
            '1 - for addition \n'
            '2 - for multiplication \n'
#            '3 - for subtraction \n'                    # работает только для положительного итогового значения
#            '4 - for dividion \n'                       # не работает
            'press any other key - you`ll get your prize \n'
            )

if dst == '1':
    print(f'Sum = {convert_to_0x(convert_from_0x(nmbr_1) + convert_from_0x(nmbr_2))}')
elif dst == '2':
    print(f'Mult = {convert_to_0x(convert_from_0x(nmbr_1) * convert_from_0x(nmbr_2))}')
# elif dst == '3':
#    print(f'Sub = {convert_to_0x(convert_from_0x(nmbr_1) - convert_from_0x(nmbr_2))}')
# elif dst == '4':
#    print(f'Div = {convert_to_0x(convert_from_0x(nmbr_1) / convert_from_0x(nmbr_2))}')
else:
    print('You could never win! Fatality, brutality, animality, formatality C:\ ')