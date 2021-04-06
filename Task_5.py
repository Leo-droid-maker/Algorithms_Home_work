import random as rd

SIZE = 20
MIN_ITEM = -50
MAX_ITEM = 50
array = [rd.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

a = MIN_ITEM

for i in range(SIZE):
    if 0 > array[i] > a:
        a = array[i]

print(f'Максимальное отрицательное число: {a}')





