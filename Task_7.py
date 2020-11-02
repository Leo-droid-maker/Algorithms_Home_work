a = float(input('Введите длину стороны a: '))
b = float(input('Введите длину стороны b: '))
c = float(input('Введите длину стороны c: '))

if a + b > c and a + c > b and b + c > a:
    print(f'Треугольник со сторонами a = {a}, b = {b}, c = {c} существует')
    if a == b == c:
        print('Треугольник равносторонний')
    elif (a == b) or (a == c) or (b == c):
        print('Треугольник равнобедренный')
    elif a != b and a != c and b != c:
        print('Треугольник разносторонний')
else:
    print('Треугольник не существует')



