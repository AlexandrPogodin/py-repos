a = [int(i) for i in input().split()]
i=0
a.sort()
res= []
while i < len(a):
    if a.count(a[i])>1 and a[i] not in res:
        res.append(a[i])
    i+=1
i=0
while i < len(res):
        print(res[i] , end=' ')
        i+=1