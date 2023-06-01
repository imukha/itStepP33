'''# lambda arg2, arg2, ...,: expression
m = lambda a, d: a / d
print(m(4, 2))
'''

'''mult = lambda a, b, c: a * b * c
result = mult(5, 2, 9)
print(result)


def mult2(a, b, c):
    return a * b * c


print(mult2(5, 2, 9))
result = mult2(5, 2, 9)
print(result)
'''
'''
import math

abs = lambda a, b: math.sqrt(a * a + b * b)
result = abs(9, 7)
print(result)'''

'''discr = lambda a, b, c: b * b - 4 * a * c
print(discr(3, 4, 5))
'''
'''import random

spysok = [
    lambda: random.random(),
    lambda: random.random(),
    lambda: random.random()
]

for i in spysok:
    print(i())
'''

'''cort = (
    lambda x: x * 2,
    lambda x: x * 3,
    lambda x: x * 5
)

for i in cort:
    print(i(3))

for i in cort:
    print(i('qwerty'))
'''
# '''
# slownyk = {
#     1: (lambda: print('Понеділок')),
#     2: (lambda: print('Вівторок')),
#     3: (lambda: print('Середа')),
#     4: (lambda: print('Четвер')),
#     5: (lambda: print('Пятниця')),
#     6: (lambda: print('Субота')),
#     7: (lambda: print('Неділя')),
# }
#
# answer = int(input('число'))
# try:
#     slownyk[answer]()
# except KeyError:
#     print('error')
# '''
'''import math

area = {'cir': (lambda r: math.pi * r * r),
        'rec': (lambda a, b: a * b),
        'tt': (lambda a, b, h: (a + b) * h / 2.0)}
answer = input('ddtlsnm')
if answer.lower() == 'cir':
    answer1 = int(input('ddtlsnm r'))
print('Площа круга = ', area['cir'](2))
print('Площа трикутника = ', area['rec'](10, 13))
print('Площа трапеції = ', area['tt'](7, 5, 3))
'''
'''summ = lambda a=1, b=2, c=3: a + b + c
print(summ())
print(summ(5))
print(summ(10, 20))
print(summ(10, 20, 25))
'''
'''
import random


def randomNumber():
    n = random.random()
    res = lambda: int(n * 100)
    return res()


print(randomNumber())
'''
'''
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else "Infinity",
    "square": lambda x: x ** 2
}

while True:
    calculator = lambda op, *args: operations[op](*args)

    op = input("Введіть операцію (+, -, *, / або square): ")
    if op == "square":
        x = float(input("Введіть число для обчислення квадрату: "))
        result = calculator(op, x)
    else:
        x = float(input("Введіть перше число: "))
        y = float(input("Введіть друге число: "))
        result = calculator(op, x, y)

    print(result)
'''
'''
minimum = (lambda a, b, c: a if (a <= b) and (b <= c) else (b if (b <= a) and (b <= c) else c))
print(minimum(21, 34, 56))
print(minimum(34, 21, 56))
print(minimum(3, 32, 1))
'''

'''
def mnoj2(x):
    return x * 2


spysok = [6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
spysok2 = list(map(mnoj2, spysok))
print(spysok2)

spysok3 = list(map((lambda x: x * 2), spysok))
print(spysok3)
'''
'''
cort = (2.88, -5.97, 9.78)

cort2 = tuple(map((lambda x: int(x)), cort))
print(cort2)
'''
'''
import re

spys1 = 'Bob Anna Alice Alex Gena Bob'
spys2 = 'adc qwe rty gfd'
viraz = re.compile('Bob')
viraz2 = re.compile('qwe')

math1 = viraz.search(spys1)
print(math1)
math2 = viraz.search((spys2))
print(math2)
math3 = viraz.finditer(spys1)
for i in math3:
    print(f'match1 - {i}')

math4 = viraz.findall(spys1)
print(math4)
print(len(math4))

poshuk = re.compile('rty')
new = poshuk.sub('HHHHH', spys2)
print(new)
'''
#
# import re
#
# rech = 'По всім питанням писати на почту qwerty_1@gmail.com, або на newadres@ukr.net, або на itstep@outluc.com'
# emails = re.findall(r"\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}", rech)
# # \w цифри букви і знак нижнього підкреслення
# for i in emails:
#     print(i)


import tkinter as tk
import re

rech = 'По всім питанням писати на почту qwerty_1@gmail.com, або на newadres@ukr.net, або на itstep@outluc.com'
login_patter = re.compile(r"^\w{3.20}@[a-z]{2,10}\.[a-z]{2,6}$")
password_pattern = re.compile(r'^\w{8,16}$')
# ^ - початок рядка
# $ - рядок закінчився
root = tk.Tk()
root.geometry('600x450+950+500')
root.resizable(False, False)


def logining():
    pass


login_lable = tk.Label(root, text='Login:', font=('Arial', 14), padx=50)
password_lable = tk.Label(root, text='Password:', font=('Arial', 14), padx=50)
root.grid_columnconfigure(0, minsize=150)

login_lable.grid(column=0, row=0)
password_lable.grid(column=0, row=1)
root.mainloop()
