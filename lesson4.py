# numbers = []
# while True:
#     user_input = input("Введіть число або 'y', щоб підсумувати: ")
#     if user_input == 'y':
#         break
#     try:
#         number = float(user_input)
#         numbers.append(number)
#     except ValueError:
#         print("Будь ласка, введіть число або 'y'.")
#
# sum_numbers = sum(numbers)
# print("Сума введених чисел: ", sum_numbers)
#
# number = input('Введіть ціле число - ')
#
# while type(number) != int:
#     try:
#         number = int(number)
#     except ValueError:
#         print('Не правильний ввід ...')
#         number = input('Введіть ціле число - ')
#
# print('Ok')


'''x = 5

for i in 2, 3, 4:
    x += i
    print(f'{i} --> x = {x}')'''
#
# x = 5
# for i in range(5):
#     x += 5
#     print(f'{i} --> x = {x}')

'''for i in range(1, 11):
    print('i - ', i)
    
for i in range(1, 11, 2):
    print('i - ', i)

n = 2
for i in range(1, 11, n):
    print('i - ', i, end=' ')
    if i % 2 == 0:
        print('Парне \n')
    else:
        print('Непарне \n')

str = 'strings'
print(len(str))
print(str[0])
print(str[-7:6:2])
x = 0
for i in range(len(str)):
    print(str[i])

lst = [27, 35,'name', ['para', 45], 554]
for i in lst:
    print(i)
print(lst[3][0])

str = input('Введіть якийсь ядок >> ')
for i in  str:
    print(str)

line = input('Введіть якийсь ядок >> ')
for c in  line:
    print(c)

line = input('Введіть якийсь ядок >> ')
for c in  line[0::2]:
    print(c)

for i in  range(1, 10):
    for j in range(1, 10):
        print(f'i*j = {i * j}', end='\t')
    print('\n')'''

floor = 1
energy = 70
while floor != 30:
    print('floor bef - ', floor)
    step = 0
    while step != 20:
        step += 1
        energy -= 1
        if energy == 0:
            print('Відпочинок!!!')
            energy += 70
    floor += 1
    print('floor', floor)
print('floor = 5')






