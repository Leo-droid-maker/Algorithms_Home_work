import random as rd

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 20
array = [rd.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

a = [i for i, item in enumerate(array) if item % 2 == 0]

print(f'индексы четных элементов списка: {a}')
