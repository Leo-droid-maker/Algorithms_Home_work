from collections import deque, OrderedDict

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


first = deque(list(input('Введите первое шестнадцатиричное число в нижнем регистре: ')))
second = deque(list(input('Введите второе шестнадцатиричное число в нижнем регистре: ')))

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







