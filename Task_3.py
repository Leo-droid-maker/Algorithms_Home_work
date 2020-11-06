x = int(input('Введите целое положительное число: '))
res = ''

while x > 0:
    temp = str(x % 10)
    res = res + temp
    x //= 10

print(int(res))


