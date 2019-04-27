def leap(a):
    if ((a % 4) == 0) and ((a % 100) != 0):
        print('Високосный')
    elif ((a % 400) == 0):
        print('Високосный')
    else:
        print('Обычный')

print('Введите год')
n = int(input())

if (n>=1900) and (n<=3000):
    leap(n)
else:
    print('Вы ввели неверный год')