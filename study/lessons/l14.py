def encode(line):
    res = ''; cnt = 0; i = 0
    temp = line[0]
    for i in range(len(line)):
        if line[i] == temp:
            cnt += 1
        else:
            res = res + temp + str(cnt)
            temp = line[i]
            cnt = 1
    res = res + temp + str(cnt)
    return res

c = str(input())
print(encode(c))
