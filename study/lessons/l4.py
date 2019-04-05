def triangle(a,b,c):
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c)) ** 0.5
    return s

flat = str(input())

if flat == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    print(triangle(a,b,c))
elif flat == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a*b)
elif flat == 'круг':
    r = int(input())
    pi = 3.14
    s = pi * r * r
    print(s)