# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

nat_chisl = int(input('Друже, введи натуральное число: '))
nat_chisl_rev = 0
while nat_chisl > 0:
    nat_chisl_rev = nat_chisl_rev * 10 + nat_chisl % 10
    nat_chisl = nat_chisl // 10
print(f'Поздравляю, получи {nat_chisl_rev}')