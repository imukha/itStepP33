#region Task_1
number_1 = input('Введіть перше число: ')
number_2 = input('Введіть друге число: ')
number_3 = input('Введіть третє число: ')
print(number_1+number_2+number_3)
#endregion
#region Task_2
number = input("Введіть любе число: ")
product = 1
for digit in number:
    product *= int(digit)
print("Добуток цифр: ", product)
#endregion
#region Task_3
meters = float(input('Введіть кількість метрів: '))
cm = meters*100
dm = meters * 10
mm = meters * 1000
miles = meters * 0.000621371192
print('В', meters, 'метрах:')
print(cm, 'сантиметрів;')
print(dm, 'дециметрів;')
print(mm, 'міліметрів;')
print(round(miles, 4), 'миль.')
#endregion
#region Task_4
base = float(input("Введіть довжину основи трикутника: "))
height = float(input("Введіть висоту трикутника: "))
area = 0.5 * base * height
print("Площа трикутника дорівнює:", area)
#endregion
#region Task_5
number = input("Введіть число: ")
reverse = ''.join(reversed(number))
print("Перевернуте число:", reverse)
#endregion
