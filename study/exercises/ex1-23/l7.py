t = str(input())

left = int(t[0]) + int(t[1]) + int(t[2])
right = int(t[3]) + int(t[4]) + int(t[5])

if (left == right):
    print('Счастливый')
else:
    print('Обычный')