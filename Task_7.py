import random as rd

SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 5
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


