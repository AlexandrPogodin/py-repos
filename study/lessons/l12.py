# a,b = input().split()
a = int(input())
b = int(input())
sm = []
for i in range(a,b+1):
    if (i % 3 == 0):
        sm.append(i)
l=len(sm)
sum = 0
for i in range(l):
    sum += sm[i]
print(sum/l)
