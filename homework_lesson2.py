reset = 'y'
while reset == 'y':
    calculations = input('Оберіть тип розрахунків: \n\t1 - Математичні \n\t2 - Конвертер одиниць довжини\n>>> ')
    if calculations == '1':
        number_1 = float(input('Введіть перше число: '))
        number_2 = float(input('Введіть друге число: '))
        number_3 = float(input('Введіть третє число: '))
        action = input('Оберіть дію яку необхідно виконати: \n\t1 - Вирахувати суму; \n\t2 - Вирахувати добуток;'
                       '\n\t3 - Вирахувати максимум; \n\t4 - Вирахувати мінімум; '
                       '\n\t5 - Вирахувати середньоарифметичне;\n>>> ')
        if action == '1':
            result = number_1 + number_2 + number_3
        elif action == '2':
            result = round(number_1 * number_2 * number_3, 2)
        elif action == '3':
            result = number_1
            if result < number_2:
                result = number_2
            if result < number_3:
                result = number_3
        elif action == '4':
            result = number_1
            if result > number_2:
                result = number_2
            if result > number_3:
                result = number_3
        elif action == '5':
            result = round((number_1 + number_2 + number_3) / 3, 3)
        else:
            result = 'Невірно обрана дія. '
    elif calculations == '2':
        miles = 0.000621371192
        inches = 39.3700787
        yards = 1.0936133
        meters = float(input('Введіть довжину в метрах: '))
        action = input('Оберіть одиниці вимірювання: \n\t1 - Милі; \n\t2 - Дюйми; \n\t3 - Ярди;\n>>> ')
        if action == '1':
            result = round(meters * miles, 4)
            result = str(result) + ' Миль'
        elif action == '2':
            result = round(meters * inches, 2)
            result = str(result) + ' Дюйма'
        elif action == '3':
            result = round(meters * yards, 2)
            result = str(result) + ' Ярдів'

        else:
            result = 'Невірно обрана дія. '
    else:
        result = 'Невірно обрана дія. '

    print(result)
    reset = input('Введіть "y", щоб продовжити, або будь-яку іншу клавішу, щоб завершити \n>>> ')
