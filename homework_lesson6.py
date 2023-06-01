# Task_1

# створюємо список з випадкових цілих чисел
import random

rand_num = []

for i in range(10):
    rand_num.append(random.randint(-10, 10))

print('Список чисел:', rand_num)

# Сума від'ємних чисел
negative_sum = sum([num for num in rand_num if num < 0])

print("Сума від'ємних чисел: ", negative_sum)

# Сума парних чисел
even_sum = sum([num for num in rand_num if num % 2 == 0])

print('Сума парних чисел: ', even_sum)

# Сума непарних чисел
odd_sum = sum([num for num in rand_num if num % 2 != 0])

print('Сума непарних чисел: ', odd_sum)

# Добуток елементів з індексами, кратними 3
index_multiply = 1

for i in range(len(rand_num)):
    if i % 3 == 0:
        index_multiply *= rand_num[i]

print('Добуток елементів з індексами, кратними 3: ', index_multiply)

# Добуток елементів між мінімальним та максимальним елементом
min_index = rand_num.index(min(rand_num))
max_index = rand_num.index(max(rand_num))

if min_index > max_index:
    min_index, max_index = max_index, min_index

multiply = 1
for i in range(min_index + 1, max_index):
    multiply *= rand_num[i]

print('Добуток елементів між мінімальним та максимальним елементом: ', multiply)

# Сума елементів, що знаходяться між першим та останнім додатним елементом
positive_indexes = [index for index, number in enumerate(rand_num) if number > 0]

if len(positive_indexes) >= 2:
    between_sum = sum(rand_num[positive_indexes[0] + 1:positive_indexes[-1]])

if len(positive_indexes) >= 2:
    print("Сума елементів, що знаходяться між першим та останнім додатним елементом: ", between_sum)

else:
    print("У списку немає двох додатніх елементів")

# Task_2

random_list = rand_num
# парні числа зі списку

even_list = []

for num in random_list:
    if num % 2 == 0:
        even_list.append(num)

print('парні числа зі списку:', even_list)

# непарні числа зі списку
odd_list = []

for num in random_list:
    if num % 2 != 0:
        odd_list.append(num)

print('непарні числа зі списку:', odd_list)

# від’ємні числа зі списку
negative_list = []

for num in random_list:
    if num < 0:
        negative_list.append(num)

print("від'ємні числа зі списку:", negative_list)

# додатні числа зі списку

positive_list = []

for num in random_list:
    if num > 0:
        positive_list.append(num)

print('додатні числа зі списку:', positive_list)
