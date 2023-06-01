'''a = 2
print(f'id(2) - {id(2)}')
print(f'id(a) - {id(a)}')

a += 1
print(f'id(a) - {id(a)}')
print(f'id(3) - {id(3)}')

d = 2
print(f'id(d) - {id(d)}')
'''

'''# ver_1 = 5


def func_1():
    global ver_1
    ver_1 = 10
    print(f'var_1 in func - {ver_1}')

func_1()
print(ver_1)
'''

'''var_1 = 5


def func_2():
    var_1 = 2
    print(var_1)

func_2()

'''
'''
print(f'loc - {locals()}')
print(f'glob - {globals()}')
'''

'''
def black_hole(*args):
    print(type(args))
    for argument in args:
        print(argument)


args = 3, 5, 18, 'name', 'adres', 4 * 5, True
args_1 = set(args)

black_hole(3, 5, 18, 'name', 'adres', 4 * 5, True)
black_hole(args)
print(args_1)
'''

import random


def bulls_and_cows(secret, guess, attempt=1):
    """
    Функція, яка порівнює задумане число зі здогадкою гравця і повертає кількість
    биків (відгаданих цифр у правильних позиціях) та корів (відгаданих цифр,
    але не у правильній позиції).

    :param secret: задумане число (стрічка)
    :param guess: здогадка гравця (стрічка)
    :param attempt: кількість спроб гравця (за замовчуванням - 1)
    :return: кортеж з кількістю биків і корів, а також кількістю спроб гравця
    """
    if len(guess) != len(secret):
        print("Некоректна кількість цифр! Введіть чотиризначне число.")
        return bulls_and_cows(secret, input("Введіть число: "), attempt)

    bulls = sum([secret[i] == guess[i] for i in range(len(secret))])
    cows = sum([guess.count(digit) - secret.count(digit) for digit in set(guess)])

    if bulls == 4:
        print(f"Вітаємо! Ви вгадали число з {attempt} спроб.")
        return (bulls, cows, attempt)
    else:
        print(f"Биків: {bulls}, корів: {cows}")
        return bulls_and_cows(secret, input("Введіть число: "), attempt + 1)


# Задумуємо чотиризначне число
secret = "".join(random.sample("0123456789", 4))
print("Я задумав чотиризначне число. Спробуйте вгадати його.")

# Починаємо гру
bulls_and_cows(secret, input("Введіть число: "))
