from sys import getsizeof
import random as rd

# Версия интерпретатора 3.8.5 и ОС 64-х битная

N = 10
SIZE = 4**N
MIN_ITEM = 1000
MAX_ITEM = 30000
array = [rd.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

if array[0] > array[1]:
    min_1_idx = 0
    min_2_idx = 1
else:
    min_1_idx = 1
    min_2_idx = 0


for i in range(SIZE):
    if array[min_1_idx] >= array[i]:
        min_2_idx = min_1_idx
        min_1_idx = i
    elif array[min_2_idx] >= array[i]:
        min_2_idx = i

print(f'Минимальные числа: {array[min_1_idx]}, {array[min_2_idx]}'
      if array[min_1_idx] != array[min_2_idx]
      else f'В списке 2 минимальных числа равных: {array[min_1_idx]}')


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


print(show(SIZE, MIN_ITEM, MAX_ITEM, array, min_1_idx, min_2_idx, i))

# Простой пример:

# [29077, 24784, 10243, 14574]
# Минимальные числа: 10243, 14574
# type(x)=<class 'int'>, getsizeof(x)=28, x=4
# type(x)=<class 'int'>, getsizeof(x)=28, x=1000
# type(x)=<class 'int'>, getsizeof(x)=28, x=30000
# type(x)=<class 'list'>, getsizeof(x)=88, x=[29077, 24784, 10243, 14574]
# type(x)=<class 'int'>, getsizeof(x)=28, x=29077
# type(x)=<class 'int'>, getsizeof(x)=28, x=24784
# type(x)=<class 'int'>, getsizeof(x)=28, x=10243
# type(x)=<class 'int'>, getsizeof(x)=28, x=14574
# type(x)=<class 'int'>, getsizeof(x)=28, x=2
# type(x)=<class 'int'>, getsizeof(x)=28, x=3
# type(x)=<class 'int'>, getsizeof(x)=28, x=3
# Обьем памяти: 720

# Пример с увеличенным числом N:

# Вставляю только последние строки вывода, тк вывод просто гигантский
# type(x)=<class 'int'>, getsizeof(x)=28, x=23573
# type(x)=<class 'int'>, getsizeof(x)=28, x=27748
# type(x)=<class 'int'>, getsizeof(x)=28, x=7318
# type(x)=<class 'int'>, getsizeof(x)=28, x=23953
# type(x)=<class 'int'>, getsizeof(x)=28, x=1045624
# type(x)=<class 'int'>, getsizeof(x)=28, x=1036019
# type(x)=<class 'int'>, getsizeof(x)=28, x=1048575
# Обьем памяти: 46755472

print('Вывод: Так как этот пример имеет только числа int и список list, при небольшом числе N код выполняется быстро'
      ' и не занимает много места. Пр увеличении длины списка обьем значительно увеличивается нетолько за счет '
      'количества элементов, но и из-за выделяемой под него памяти "с запасом". Так же как и в примере с матрицей,'
      'не имея контроля за размером списка, можно получить неприятные последствия в дальнейшем, связанные с нехваткой '
      'памяти и быстродействием.')
