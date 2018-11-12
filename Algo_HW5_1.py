# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль
# выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
# Примечание: 4 квартала - это 4 разных прибыли ;-)

from collections import namedtuple

Company = namedtuple('Company',                            # создаем класс Company
                     'name, profit_q1, profit_q2,'
                     'profit_q3, profit_q4, ltm')          # ltm = last twelve month (правильно писать LTM)

n = int(input('Number of companies: '))                    # вводим колличество компаний
if n == 0:                                                 # проверяем на введенный 0
    print('WTF?! -_-')
    exit()
count = 0                                                  # счетчик для вычисления LTM
middle_count = 0                                           # счетчик для middle LTM по всем компаниям

comp_lst = [[None for j in range(5)] for i in range(n)]    # генератор списка. Без него не знаю как заставить
                                                           # цикл заполнения показателей (стр 27-36) работать :(
comp_lst_comp = comp_lst.copy()                            # создание копии списка для будущего учета класса Company,

higher_lst = []
middle_lst = []
lower_lst = []

for i in range(n):                                         # цикл заполнения показателей
    comp_lst[i][0] = input(f'Input {i+1} company name: ')  # коряво
    for j in range(1, 5):
        comp_lst[i][j] = int(input(f'Please, Sir, input {i+1} company profit for the {j} quarter: '))
        count += comp_lst[i][j]
    print(f'{1} company LTM profit equals {count}')
    comp_lst[i].append(count)
    middle_count += count
    count = 0
    comp_lst_comp[i] = Company._make(comp_lst[i])          # на составление цикла и этой строки ушло жутко много времени
                                                           # Если есть более оптимальный способ заполнения namedtuple,
                                                           # расскажите, пожалуйста.
middle_count /= n       # вычисление среднего LTM
print(f'Middle profit = {middle_count}')

for i in range(n):                                         # цикл разнесения по спискам, в зависимости от LTM
    if comp_lst_comp[i].ltm < middle_count:
        lower_lst.append(comp_lst_comp[i].name)
    elif comp_lst_comp[i].ltm > middle_count:
        higher_lst.append(comp_lst_comp[i].name)
    else:
        middle_lst.append(comp_lst_comp[i].name)
print(f'Higher results: {higher_lst}; lower results: {lower_lst}; middle results: {middle_lst}')