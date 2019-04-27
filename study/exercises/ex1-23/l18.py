t = 1
sum = 0
sumq = 0
while t !=0:
    a = int(input())
    sum+=a
    sumq+= a ** 2
    if sum == 0:
        t = 0
print(sumq)
