print('Введите числа и операцию')
x = float(input())
y = float(input())
op = str(input())

if (op == '+'):
    print(x + y)
elif (op == '-'):
    print(x - y)
elif (op == '/'):
    if (y == 0):
        print('Деление на 0!')
    else:
        print(x / y)
elif (op == '*'):
    print(x*y)
elif (op == 'mod'):
    if (y == 0):
        print('Деление на 0!')
    else:
        print(x % y)
elif (op == 'pow'):
    print(x ** y)
elif (op == 'div'):
    if (y == 0):
        print('Деление на 0!')
    else:
        print(x // y)