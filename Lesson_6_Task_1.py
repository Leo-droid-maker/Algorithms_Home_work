import timeit
from sys import getsizeof
from random import randint

# Версия интерпретатора 3.8.5 и ОС 64-х битная

N = 10
LINES = 4**N
SIZE = 4
MIN_ITEM = 1000
MAX_ITEM = 30000

print('Создайте матрицу, добаляя в неё числа.')
print('-' * 100)
print('Матрица 5х4, где 4-й столбец содержит сумму значений в строке.')

matrix = []
# print(f'размер пустого списка matrix {getsizeof(matrix)}') - использовал для проверки
for i in range(LINES):
    a = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    matrix.append(a)
    # print(f'размер matrix {getsizeof(matrix)}') - использовал для проверки


# print(*matrix, sep='\n')

for line in matrix:
    sum_line = 0
    for i in line:
        sum_line += i
        print(f'{i:>5}', end='')
    print(f'\t{sum_line:>5}')

print('-' * 30)


def show(*args):
    tmp_res = getsizeof(args)
    for x in args:
        print(f'{type(x)=}, {getsizeof(x)=}, {x=}')
        tmp_res += getsizeof(x)
        if hasattr(x, '__iter__'):
            if hasattr(x, 'items'):
                for key, value in x.items():
                    show(key)
                    tmp_res += getsizeof(key)
                    show(value)
                    tmp_res += getsizeof(value)
            elif not isinstance(x, str):
                for item in x:
                    show(item)
                    tmp_res += getsizeof(item)
        tmp_res += getsizeof(x)  # без этой строки, если сложить вручную, получается другое значение
    return f'Обьем памяти: {tmp_res}'


print(show(matrix, LINES, i, sum_line, line))

# Простой пример:

# Создайте матрицу, добаляя в неё числа.
# ----------------------------------------------------------------------------------------------------
# Матрица 5х4, где 4-й столбец содержит сумму значений в строке.
# размер пустого списка matrix 56
# Введите три числа через пробел: 1 1 1
# размер matrix 88
# Введите три числа через пробел: 2 2 2
# размер matrix 88
# Введите три числа через пробел: 3 3 3
# размер matrix 88
# Введите три числа через пробел: 4 4 4
# размер matrix 88
# Введите три числа через пробел: 5 5 5
# размер matrix 120
#     1    1    1	    3
#     2    2    2	    6
#     3    3    3	    9
#     4    4    4	   12
#     5    5    5	   15
# ------------------------------
# type(x)=<class 'list'>, getsizeof(x)=120, x=[[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]]
# type(x)=<class 'list'>, getsizeof(x)=104, x=[1, 1, 1]
# type(x)=<class 'int'>, getsizeof(x)=28, x=1
# type(x)=<class 'int'>, getsizeof(x)=28, x=1
# type(x)=<class 'int'>, getsizeof(x)=28, x=1
# type(x)=<class 'list'>, getsizeof(x)=104, x=[2, 2, 2]
# type(x)=<class 'int'>, getsizeof(x)=28, x=2
# type(x)=<class 'int'>, getsizeof(x)=28, x=2
# type(x)=<class 'int'>, getsizeof(x)=28, x=2
# type(x)=<class 'list'>, getsizeof(x)=104, x=[3, 3, 3]
# type(x)=<class 'int'>, getsizeof(x)=28, x=3
# type(x)=<class 'int'>, getsizeof(x)=28, x=3
# type(x)=<class 'int'>, getsizeof(x)=28, x=3
# type(x)=<class 'list'>, getsizeof(x)=104, x=[4, 4, 4]
# type(x)=<class 'int'>, getsizeof(x)=28, x=4
# type(x)=<class 'int'>, getsizeof(x)=28, x=4
# type(x)=<class 'int'>, getsizeof(x)=28, x=4
# type(x)=<class 'list'>, getsizeof(x)=104, x=[5, 5, 5]
# type(x)=<class 'int'>, getsizeof(x)=28, x=5
# type(x)=<class 'int'>, getsizeof(x)=28, x=5
# type(x)=<class 'int'>, getsizeof(x)=28, x=5
# type(x)=<class 'int'>, getsizeof(x)=28, x=5
# type(x)=<class 'int'>, getsizeof(x)=28, x=5
# type(x)=<class 'int'>, getsizeof(x)=28, x=15
# type(x)=<class 'list'>, getsizeof(x)=104, x=[5, 5, 5]
# type(x)=<class 'int'>, getsizeof(x)=28, x=5
# type(x)=<class 'int'>, getsizeof(x)=28, x=5
# type(x)=<class 'int'>, getsizeof(x)=28, x=5
# Обьем памяти: 1300
#
# Process finished with exit code 0

# Пример с увеличенным числом N:

# Вставляю только последние строки вывода, тк вывод просто гигантский
# type(x)=<class 'int'>, getsizeof(x)=28, x=14357
# type(x)=<class 'int'>, getsizeof(x)=28, x=18613
# type(x)=<class 'int'>, getsizeof(x)=28, x=3053
# type(x)=<class 'int'>, getsizeof(x)=28, x=2281
# type(x)=<class 'int'>, getsizeof(x)=28, x=12091
# type(x)=<class 'int'>, getsizeof(x)=28, x=18472
# type(x)=<class 'int'>, getsizeof(x)=28, x=23076
# Обьем памяти: 90242816


# при N = 10
print(timeit.timeit('show(matrix)', number=1, globals=globals()))  # 49.85382755300088
print(timeit.timeit('show(matrix)', number=2, globals=globals()))  # 105.3329333340007
print(timeit.timeit('show(matrix)', number=5, globals=globals()))  # 152.7859147229974


print('Вывод: На примере добавления в список элементов, можно заметить то, что вы говорили на уроке:'
      'изначально под список выделяется определенное кол-во памяти на 4 элемента, но при добавлении 5-го,'
      'для списка добавляется еще памяти. При увеличении значений чисел, их обьем в памяти никак не меняется (тип int),'
      'но при увеличении числа N, как в этом примере, обьем данных возрастает многократно (при N = 10, было '
      'задействованно более 90 мб, и выполняется крайне медленно (но, как я могу предположить, зависимость линейная.')
