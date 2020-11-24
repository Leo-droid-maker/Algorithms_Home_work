import random as rd

SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 20
array = [rd.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_index = 0
min_index = 0

for i in range(SIZE):
    if array[i] > array[max_index]:
        max_index = i
    elif array[i] < array[min_index]:
        min_index = i

print(f'Меняем местами элементы с индексами: {max_index}, {min_index}')

array[max_index], array[min_index] = array[min_index], array[max_index]

print(array)






