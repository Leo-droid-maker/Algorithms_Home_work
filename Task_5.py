c1 = input('Введите любую букву английского алфавита от a до z включительно: ')
c2 = input('Введите еще раз букву английского алфавита от a до z включительно: ')

num1 = ord(c1)
num2 = ord(c2)
res1 = 0

if num1 != num2:
    res1 = abs(num1 - num2) - 1
    res2 = (num1 - 97) + 1
    res3 = (num2 - 97) + 1
    print(f'Мужду буквами {c1} и {c2} расположено {res1} букв')
    print(f'Буква {c1} в алфавите располагается на {res2} месте.\nБуква {c2} в алфавите располагается на {res3} месте.')
else:
    print('Буквы одинаковы, повторите попытку и введите разные буквы')