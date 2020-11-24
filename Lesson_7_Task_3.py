from random import randint

MIN_ITEM = 1
MAX_ITEM = 10
M = randint(MIN_ITEM, MAX_ITEM)
SIZE = (2 * M) + 1
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


class Colors:
    RED = '\033[91m'


class GnomeSort(Colors):

    def __init__(self, arr):
        self.arr = arr

    def gnome_sort(self):
        n = (len(self.arr) + 1) // 2  # формула медианы
        row = 1
        size = len(self.arr)
        while row < size:  # пока гном не пройдет все ряды с горшками
            if self.arr[row - 1] <= self.arr[row]:  # если порядок горшков правильный, то гном переходит дальше
                row += 1
            else:
                self.arr[row - 1], self.arr[row] = self.arr[row], self.arr[row - 1]  # иначе гном меняет горшки местами
                # и возвращается назад
                if row > 1:  # если ряд не первый
                    row -= 1

        return f'Медиана: {n}-й элемент списка (не индекс) {self.arr} со значением {Colors.RED}{self.arr[n - 1]}'


result = GnomeSort(array)
print(f'Изначальный список: {array}')
print(result.gnome_sort())
