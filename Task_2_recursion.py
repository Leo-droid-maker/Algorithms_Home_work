x = int(input('Введите натуральное число (целое, больше 0) любой длины: '))
odd = 0
even = 0


def rec(number):
    global odd, even
    while number != 0:
        last_num = number % 10
        if last_num % 2 == 0:
            even += 1
            return rec(number // 10)
        else:
            odd += 1
            return rec(number // 10)
    return f'Нечетных цифр в введенном числе: {odd}. Четных цифр: {even}'


print(rec(x))
