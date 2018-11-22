# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N. Например, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()


'''Отличного Вам отпуска Алексей. Вы реально классный преподаватель,
могу это сказать с учетом собственного оптыта преподавания во время учебы аспирантуре'''

import random
import string
import hashlib

def str_generator(N, chars=string.ascii_lowercase):             # генерируем строку
    return ''.join(random.choice(chars) for _ in range(N))


def dict_hash_key(S):                                           # формируем словарь для учета подстрок через хэш-ключ
    lst = {}
    spam = hash_hex_magic(S)
    for i in range(len(S)):
        for j in range(len(S)):
            if hash_hex_magic(S[i:i + j + 1]) in lst:
                continue
            else:
                if hash_hex_magic(S[i:i + j + 1]) != spam:
                    lst[hash_hex_magic(S[i:i + j + 1])] = S[i:i + j + 1]
    return lst

def hash_hex_magic(x):                                          # колдуем хэш
    x = hashlib.sha1(bytes(x.encode('utf-8'))).hexdigest()
    return x

N = int(input('Введите длину строки: '))
S = str_generator(N)
DICT = dict_hash_key(S)
print(f'В строке "{S}" находится {len(DICT)} подстрок: {DICT.values()}, не считая самой строки "{S}"')


# Ради шутки ниже решение задачи в одну строку без хэширования ;)

print(f'{len(set([S[i:i + j + 1] for j in range(len(S)) for i in range(len(S)) if S != S[i:i + j + 1]]))} подстрок')
