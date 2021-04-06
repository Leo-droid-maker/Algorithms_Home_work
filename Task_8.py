user_year = int(input('Введите год для проверки на високосность: '))

if (user_year % 400 == 0) and (user_year % 100 == 0) and (user_year % 4 == 0):
    print('Год високосный')
elif user_year % 4 == 0:
    if user_year % 100 == 0:
        print('Год невисокосный')
    else:
        print('Год високосный')
else:
    print('Год невисокосный')
