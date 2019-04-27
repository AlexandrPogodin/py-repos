n = 0
a = []
while n <= 100:
    n = int(input())
    if n < 10:
        continue
    if n > 100:
        break
    a.append(str(n))

l = len(a)
i = 0
while i < l:
    print(a[i])
    i += 1