from collections import deque, OrderedDict
from sys import getsizeof

# Версия интерпретатора 3.8.5 и ОС 64-х битная

REG = OrderedDict(
    {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15,
        '10': 16
    }
)


first = deque(list('a2'))
second = deque(list('c4f'))

while len(first) != len(second):
    if len(first) > len(second):
        second.appendleft('0')
    else:
        first.appendleft('0')


# print(first, second)
result = deque()
tmp = 0

for i in range(len(first)):
    a = first.pop()
    b = second.pop()
    res = REG[a] + REG[b]
    if res > REG['10']:
        c = res - REG['10']
        if c > REG['9']:
            result.appendleft(list(REG.keys())[list(REG.values()).index(c)])
        elif tmp == 1:
            c += tmp
            result.appendleft(list(REG.keys())[list(REG.values()).index(c)])
        else:
            result.appendleft(str(res - REG['10']))
        tmp = 1
        # print(res)
    else:
        res += tmp
        # print(res)
        if res == REG['10']:
            result.appendleft('0')
            tmp = 1
        else:
            result.appendleft(list(REG.keys())[list(REG.values()).index(res)])
            tmp = 0

if tmp == 1:
    result.appendleft(str(tmp))

print(result)


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


print(show(REG, result, tmp, i, res, a, b))

# type(x)=<class 'collections.OrderedDict'>, getsizeof(x)=1504, x=OrderedDict([('0', 0), ('1', 1), ('2', 2), ('3', 3),
# ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('a', 10), ('b', 11), ('c', 12), ('d', 13), ('e', 14),
# ('f', 15), ('10', 16)])
# type(x)=<class 'str'>, getsizeof(x)=50, x='0'
# type(x)=<class 'int'>, getsizeof(x)=24, x=0
# type(x)=<class 'str'>, getsizeof(x)=50, x='1'
# type(x)=<class 'int'>, getsizeof(x)=28, x=1
# type(x)=<class 'str'>, getsizeof(x)=50, x='2'
# type(x)=<class 'int'>, getsizeof(x)=28, x=2
# type(x)=<class 'str'>, getsizeof(x)=50, x='3'
# type(x)=<class 'int'>, getsizeof(x)=28, x=3
# type(x)=<class 'str'>, getsizeof(x)=50, x='4'
# type(x)=<class 'int'>, getsizeof(x)=28, x=4
# type(x)=<class 'str'>, getsizeof(x)=50, x='5'
# type(x)=<class 'int'>, getsizeof(x)=28, x=5
# type(x)=<class 'str'>, getsizeof(x)=50, x='6'
# type(x)=<class 'int'>, getsizeof(x)=28, x=6
# type(x)=<class 'str'>, getsizeof(x)=50, x='7'
# type(x)=<class 'int'>, getsizeof(x)=28, x=7
# type(x)=<class 'str'>, getsizeof(x)=50, x='8'
# type(x)=<class 'int'>, getsizeof(x)=28, x=8
# type(x)=<class 'str'>, getsizeof(x)=50, x='9'
# type(x)=<class 'int'>, getsizeof(x)=28, x=9
# type(x)=<class 'str'>, getsizeof(x)=50, x='a'
# type(x)=<class 'int'>, getsizeof(x)=28, x=10
# type(x)=<class 'str'>, getsizeof(x)=50, x='b'
# type(x)=<class 'int'>, getsizeof(x)=28, x=11
# type(x)=<class 'str'>, getsizeof(x)=50, x='c'
# type(x)=<class 'int'>, getsizeof(x)=28, x=12
# type(x)=<class 'str'>, getsizeof(x)=50, x='d'
# type(x)=<class 'int'>, getsizeof(x)=28, x=13
# type(x)=<class 'str'>, getsizeof(x)=50, x='e'
# type(x)=<class 'int'>, getsizeof(x)=28, x=14
# type(x)=<class 'str'>, getsizeof(x)=50, x='f'
# type(x)=<class 'int'>, getsizeof(x)=28, x=15
# type(x)=<class 'str'>, getsizeof(x)=51, x='10'
# type(x)=<class 'int'>, getsizeof(x)=28, x=16
# type(x)=<class 'collections.deque'>, getsizeof(x)=624, x=deque(['c', 'f', '1'])
# type(x)=<class 'str'>, getsizeof(x)=50, x='c'
# type(x)=<class 'str'>, getsizeof(x)=50, x='f'
# type(x)=<class 'str'>, getsizeof(x)=50, x='1'
# type(x)=<class 'int'>, getsizeof(x)=24, x=0
# type(x)=<class 'int'>, getsizeof(x)=28, x=2
# type(x)=<class 'int'>, getsizeof(x)=28, x=12
# type(x)=<class 'str'>, getsizeof(x)=50, x='0'
# type(x)=<class 'str'>, getsizeof(x)=50, x='c'
# Обьем памяти: 6185
#
# Process finished with exit code 0

print('Вывод: На этом примере можно увидеть какой обьем занимают разные коллекции и типы данных (str, int)'
      'Также, несмотря на то, что словарь занимает больший обьем по сравнению с простой матрицей из файла ..Task_1,'
      'считаю, что при увеличении кол-ва шестнадцатеричных цифр (которые вводятся как str), обьем памяти не будет так '
      'сильно увеличиваться, как при увеличении размера матрицы, даже несмотря на то, что под str выделяется больше'
      'памяти чем для int.')
