from random import randint

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def bubble_sort(arr):
    n = len(arr)
    count = True
    while count and n > 0:
        count = False
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count = True
        n -= 1
        print(arr)


print(array)
bubble_sort(array)
