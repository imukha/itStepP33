restart = 'y'
while restart == 'y':
    # Task_1
    print('Завдання 1')
    try:
        numb_day = int(input('Введіть номер дня тиждня від 1 до 7\n...'))

        if numb_day == 1:
            print('Понеділок')
        elif numb_day == 2:
            print('Вівторок')
        elif numb_day == 3:
            print('Середа')
        elif numb_day == 4:
            print('Четвер')
        elif numb_day == 5:
            print('Пятниця')
        elif numb_day == 6:
            print('Субота')
        elif numb_day == 7:
            print('Неділя')
        else:
            print('Не правильний ввід')

    except:
        print('Не коректний ввід')

    # Task_2
    print('\nЗавдання 2')
    try:
        months = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень',
                  'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень']

        numb_month = int(input('Введіть номер місяця від 1 до 12\n...'))

        if numb_month >= 1 and numb_month <= 12:
            name_month = months[numb_month - 1]
            print(name_month)
        else:
            print('Не правильний ввід')

    except:
        print('Не коректний ввід')

    # Task_3
    print('\nЗавдання 3')
    try:
        number = int(input('Вееділь любе число\n... '))

        if number > 0:
            print('Number is positive')
        elif number < 0:
            print('Number is negative')
        elif number == 0:
            print('Number is equal to zero')

    except:
        print('Не коректний ввід')

    # Task_4
    print('\nЗавдання 4')
    try:
        number_1 = int(input('Введіть перше число\n...'))
        number_2 = int(input('Введіть друге число\n...'))

        if number_1 == number_2:
            print('Ці числа рівні.')
        elif number_1 > number_2:
            print(number_2, number_1)
        elif number_1 < number_2:
            print(number_1, number_2)

    except:
        print('Не коректний ввід')

    print('\nКінець')
    restart = input('Введіть "y" щоб почати з початку\n...')
