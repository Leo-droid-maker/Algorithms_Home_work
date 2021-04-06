n = int(input('Введите число элементов ряда чисел: 1, -0.5, 0.25, -0.125,… (натуральное число) для расчета суммы: '))

tmp = 1
count = 0
result = 0

while count != n:
    tmp /= -2
    result += tmp
    count += 1

print(f'Результат: {result}')



