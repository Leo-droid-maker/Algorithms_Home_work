import random as rd

try_count = 3

num = rd.randint(0, 101)

print('Добро пожаловать в игру угадай число.')
print(num)

while try_count > 0:
    print(f'Количество попыток: {try_count}')
    user_number = int(input('Введите число: '))
    if user_number == num:
        print(f'Ура, вы победили! Загаданное число: {num}')
        break
    elif user_number < num:
        print('Ваше число меньше загаданного.')
        try_count -= 1
    else:
        print('Ваше число больше загаданного.')
        try_count -= 1

print('Конец игры')


