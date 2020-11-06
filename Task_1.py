https://drive.google.com/file/d/1dVO3zAeIRk9e9_f1aVV3uzwxx-R_J3Dx/view?usp=sharing

while True:
    num1 = float(input('Enter a first number: '))
    num2 = float(input('Enter a second number: '))
    operator = input('Enter operator (+, -, *, /, 0 (zero) - for exit): ')
    if operator == '+' or operator == '-' or operator == '*' or operator == '/' or operator == '0':
        if operator == '0':
            print('Bye')
            break
        elif operator == '+':
            print(f'Result: {num1 + num2}')
        elif operator == '-':
            print(f'Result: {num1 - num2}')
        elif operator == '*':
            print(f'Result: {num1 * num2}')
        elif operator == '/' and num2 != 0:
            print(f'Result: {num1 / num2}')
        else:
            print('Zero Division error, please try again')
    else:
        print('Wrong operator, try again')


