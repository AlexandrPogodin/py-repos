print('Введите количество чисел:')
i = int(input())

sum = 0
print('\nВведите последовательность чисел построчно:\n')
while i>0:
    n = int(input())
    i-=1
    sum +=n

print('\nСумма чисел = ', sum)




# sum = 0
# n = '0'
# print('\nВведите последовательность чисел построчно:\n')
# while n!='':
#     sum += int(n)
#     n = input()

# print('\nСумма чисел = ', sum)