n = int(input())
numbers = []
nums = 0
for i in range(0,n):
    for j in range(0,i):
        if nums == n:
            break
        numbers.append(i)
        nums+=1
if n == 2:
    numbers.append(2)
if n == 1:
    numbers.append(1)
print(*numbers)
