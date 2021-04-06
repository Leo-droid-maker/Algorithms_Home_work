# https://drive.google.com/file/d/1_qP_GYozY7N53cWWVPJzEX5wJkfJSulm/view?usp=sharing

print('Получение суммы и произведения цифр трехзначного числа')
a = (int(input('Введите целое положительное трехзначное число: ')))

r1 = a // 100
r2 = int(float(a // 10) % 10)
r3 = a % 10

print(f'Сумма = {r1 + r2 + r3}, Произведение = {r1 * r2 * r3}')
