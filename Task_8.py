LINES = 5

print('Создайте матрицу, добаляя в неё числа.')
print('-' * 100)
print('Матрица 5х4, где 4-й столбец содержит сумму значений в строке.')

matrix = []
for i in range(LINES):
    a = list(map(int, input('Введите три числа через пробел: ').split()))
    matrix.append(a)

# print(*matrix, sep='\n')

for line in matrix:
    sum_line = 0
    for i in line:
        sum_line += i
        print(f'{i:>5}', end='')
    print(f'\t{sum_line:>5}')
