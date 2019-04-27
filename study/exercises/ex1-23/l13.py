str = str(input())
str = str.lower()
cnt = 0

for w in str:
    if w == 'g' or w == 'c':
        cnt += 1

print((cnt/len(str))*100)