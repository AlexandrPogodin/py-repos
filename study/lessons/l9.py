a = int(input())
b = int(input())
nod = a
while (nod % b != 0):
    nod = nod + a
print(nod)