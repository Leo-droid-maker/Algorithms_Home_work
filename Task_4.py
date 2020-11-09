import random as rd

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 20
array = [rd.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

a = MIN_ITEM

for i in range(SIZE):
    if array.count(array[i]) > array.count(a):
        a = array[i]

print(f'Первое чаще всего встречающееся число в списке: {a}')



