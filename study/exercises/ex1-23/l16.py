a = [int(i) for i in input().split()]

if len(a) == 1:
    print(a[0])
else:
    res = []
    i=0
    while i < len(a):
        if i == 0:
            temp = a[-1] + a[i+1]
        elif i == len(a)-1:
            temp = a[i-1] + a[0]
        else:
            temp = a[i-1] + a[i+1]
        res.append(temp)
        i+=1
    i=0
    while i < len(a):
        print(res[i] , end=' ')
        i+=1