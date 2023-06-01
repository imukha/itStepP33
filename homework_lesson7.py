import random

# генеруємо три кортежі випадкових цілих чисел
t1 = tuple(random.sample(range(0, 31), 20))
t2 = tuple(random.sample(range(0, 31), 20))
t3 = tuple(random.sample(range(0, 31), 20))

# виводимо кортежі на екран
print('Кортеж №1:', t1)
print('Кортеж №2:', t2)
print('Кортеж №3:', t3)

# знаходимо елементи, які є у всіх кортежах
common_elements = set(t1) & set(t2) & set(t3)

# №1 елементи, які є у всіх кортежах
print(f"Елементи, які є у всіх кортежах: {common_elements}")

# №2 елементи, які унікальні для кожного списку
print('Елементи які є тільки в Кортежі №1:', set(t1) - set(t2) - set(t3))
print('Елементи які є тільки в Кортежі №2:', set(t2) - set(t1) - set(t3))
print('Елементи які є тільки в Кортежі №3:', set(t3) - set(t2) - set(t1))
print()

# №3 елементи, якіє в кожному з кортежів і знаходяться в кожному з них на тій самій позиції.

# створили три кортежі,
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
t2 = (2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
t3 = (3, 4, 3, 5, 6, 7, 8, 9, 1, 10, 12, 13, 13, 15, 16, 16, 18, 19, 20, 10)

# цикл для перебору значень
common_elements1 = []
for i in range(min(len(t1), len(t2), len(t3))):
    if t1[i] == t2[i] == t3[i]:
        common_elements1.append(t1[i])
# Результат
print('Елементи, які є в кожному з кортежів і на тій самій позиції', common_elements1)