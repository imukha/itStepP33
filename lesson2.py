# print('1==1', 1==1)
# print('1==2', 1==2)
# print('1!=1', 1!=1)
# print('1!=2', 1!=2)
# print('1>1', 1>1)
# print('1>2', 1>2)
# print('1<1', 1<1)
# print('1<2', 1<2)
# print('1>=2', 1>=2)
# print('1<=2', 1<=2)

# print(bool(''))
# print(bool(0.0))
# print(bool(None))
# print(bool('some text'))
# print(bool(1))

# competent = True
# responsible = True
# print(competent and responsible)

# competent = True
# responsible = False
# print(competent or responsible)

# not "Логічне заперечення"
# bula_zv= True
# print(not bula_zv)
#
# bula_zv= False
# print(not bula_zv)

# time = int(input('Введіть поточний час: ')) % 24
# ticket = False
# money = True
# luggage = False
# print((money or ticket) and not luggage and time>6)
# #not -> and -> or

# car_speed = int(input('Введіть швидкість: '))
# if car_speed > 50:
#     print('Машина швидше 50км/г')


# car_speed = 100
# if car_speed > 50 and car_speed < 150:
#     print('Швидкість авто між 50 та 150км/г')
#
# car_speed = 100
# if 50 < car_speed < 150:
#     print('Швидкість авто між 50 та 150км/г')

# a, b, c = int(input("Перше: ")), int(input("Друге: ")), int(input("Третє: "))
# max = a
# if max<b:
#     max=b
# if max<c:
#     max=c
# print('максимум', max)

# if 5 > 4:
#     print('початок блоку виконання')
#     print('частина блоку виконання')
#     print('частина блоку виконання')
#     print('кінець блоку виконання')
# print('це вже не частина блоку виконання')

# car_speed = 100
# motorcycle_speed = 100
# if car_speed > motorcycle_speed:
#     print('авто швидша ніж мотоцикл')
# elif car_speed < motorcycle_speed:
#     print('мотоцикл швидший за авто')
# else:
#     print('однакова швидкість')

# number = int(input('enter the answer number'))
# if number == 1:
#     print('було обрано варіант А')
# elif number == 2:
#     print('було обрано варіант Б')
# elif number == 3:
#     print('було обрано варіант В')
# elif number == 4:
#     print('було обрано варіант Г')
# else:
#     print('Такого варіанту немає')

# myname = input('введіть логін: ')
# mypass = input('введіть пароль: ')
# if myname == 'admin ' and mypass == '1111':
#     result = 'Привіт ' + myname + ' адмін'
# elif myname == 'student ' and mypass == ' qwerty':
#     result = 'Привіт ' + myname + ' студент'
# elif myname == 'ivan ' and mypass == ' qwerty':
#     result = 'Привіт ' + myname + ' Ivan'
# else:
#     result = 'я тебе не знаю'
# print(result)

# question_1 = '2+2'
# question_2 = '3*3'
# question_3 = '5*5'
# question_4 = '2+2*2'
# answ_1 = '4'
# answ_2 = '9'
# answ_3 = '25'
# answ_4 = '6'
# result = 0
# user_anser = input(question_1)
# if user_anser == answ_1:
#     result +=1
#     print('Correct')
# else:
#     print('incorect')
#
# user_anser = input(question_2)
# if user_anser == answ_2:
#     result +=1
#     print('Correct')
# else:
#     print('incorect')
#
# user_anser = input(question_3)
# if user_anser == answ_3:
#     result +=1
#     print('Correct')
# else:
#     print('incorect')
#
# user_anser = input(question_4)
# if user_anser == answ_4:
#     result +=1
#     print('Correct')
# else:
#     print('incorect')
#
# print('you have', result, 'point')

# region CALCULATOR
reset = 'y'
while reset == 'y':
    import math

    number_1 = float(input('Введіть перше число: '))
    action = input('Введіть дію\n\t+ Додати\n\t- Відняти\n\t* Помножити\n\t/ Поділити\n\t** Піднесення до степеню'
                   '\n\t// Корінь числа\n>>> ')
    if action == '//':
        print(round(math.sqrt(number_1), 3))
    else:

        number_2 = float(input('Введіть друге число: '))
        result = 0
        if action == '+':
            result = (number_1 + number_2)
        elif action == '-':
            result = (number_1 - number_2)
        elif action == '*':
            result = (number_1 * number_2)
        elif action == '/':
            try:
            # if number_2 == 0:
            #     print('на нуль ділити не можна!!!')
            # elif number_2 != 0:
                result = (number_1 / number_2)
            except:
                print('на нуль ділити не можна!!!')
        elif action == '**':
            result = number_1 ** number_2

        else:
            print('Такої дії не існує')
        print(round(result, 3))
    reset = input('Введіть "y", щоб продовжити, або любу іншу клавішу, щоб завершити >> ')
# endregion