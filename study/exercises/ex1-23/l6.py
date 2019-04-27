n = int(input())
p = n % 10
k = n % 100

if (p >= 2) and (p <= 4) and ((k < 10) or (k > 20)):
    print(n, ' программиста')
elif (p == 1) and ((k < 10) or (k > 20)):
    print(n, ' программист')
else:
    print(n, ' программистов')