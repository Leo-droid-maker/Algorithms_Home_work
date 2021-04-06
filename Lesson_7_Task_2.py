from random import uniform

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def merge_sort(arr):
    def merge_list(left, right):
        result = []
        i = 0  # индекс для левой части
        j = 0  # индекс для правой части

        for el in range(len(left) + len(right)):  # цикл проходит [0, длина обеих частей)
            if i < len(left) and j < len(right):  # сравниваем элементы (каждый элемент - тоже список)
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            elif i == len(left):
                result.append(right[j])
                j += 1
            elif j == len(right):
                result.append(left[i])
                i += 1
        return result

    def div_list(list_to_div):  # в стеке рекурсии сохраняются неотсортированные списки, полученные делением
        if len(list_to_div) <= 1:
            return list_to_div  # возвращаем список с одним элементом

        left_part = div_list(list_to_div[:len(list_to_div) // 2])  # рекурсивно выполняем деление левой части
        right_part = div_list(list_to_div[len(list_to_div) // 2:])  # рекурсивно выполняем деление правой части

        return merge_list(left_part, right_part)  # соединяем и сортируем части в функции merge()

    return div_list(arr)


r = merge_sort(array)
print(f'Изначальный список: {array}')
print(f'Отсортированный список: {r}')

