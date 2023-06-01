while True:
    print('Оберіть завдання:\n'
          '1. - Завлання №1\n'
          '2. - Завлання №2\n'
          '3. - Завлання №3\n'
          '4. - Завлання №4\n')
    choice = input('Ваш вибір:\n-->')

    if choice == '1':
        while True:
            # Створення словника формул
            formulas = {
                '1': ('Швидкість(км/год) = Шлях(км) / Час(год)', lambda s, t: s / t),
                '2': ('Час(год) = Шлях(км) / Швидкість(км/год)', lambda s, v: s / v),
                '3': ('Шлях(км) = Швидкість(км/год) * Час(год)', lambda v, t: v * t)
            }

            # Виведення доступних формул
            print('Доступні формули: \n1 - Швидкість(км/год). \n2 - Час(год). \n3 - Шлях(км).\n4 - Вихід')

            # Вибір формули від користувача
            formula = input('Виберіть формулу:\n--> ')
            if formula == '4':
                break
            # Перевірка, чи вибрана формула присутня в словнику
            if formula in formulas:
                # Отримання формули та виведення на екран
                formula_text, formula_func = formulas[formula]
                print('Формула:', formula_text)

                # Введення користувачем даних
                data1 = float(input('Введіть перше значення: '))
                data2 = float(input('Введіть друге значення: '))

                # Виклик відповідної лямбда-функції та виведення результату
                result = formula_func(data1, data2)
                units = 'км/год' if formula == '1' else 'км' if formula == '3' else 'год'
                print('Результат:', result, units)
            else:
                print('Невідома формула')


    elif choice == '2':
        # Запитуємо у користувача ввести елементи через пробіл
        input_data = input("Введіть елементи через пробіл: ").split()

        # Конвертуємо елементи з рядка у цілі числа
        numbers = [int(element) for element in input_data]

        # Відсортовуємо список за критерієм парності
        sorted_numbers = sorted(numbers, key=lambda x: x % 2)

        # Видрукувати лише парні елементи
        even_numbers = [number for number in sorted_numbers if number % 2 == 0]
        print("Парні елементи:", even_numbers)

    elif choice == '3':
        # Запитуємо у користувача ввести елементи через пробіл
        input_data = input("Введіть елементи через пробіл: ")

        # Розбиваємо рядок на окремі елементи і конвертуємо їх у цілі числа
        numbers = [int(element) for element in input_data.split()]

        # Видрукувати лише числа, які діляться на 3
        divisible_by_3 = [number for number in numbers if number % 3 == 0]
        print("Числа, які діляться на 3:", divisible_by_3)

    elif choice == '4':
        figures = {
            'Коло': {
                'formulas': {
                    'Площа': ('Площа кола = π * (Радіус ^ 2)', lambda r: 3.14 * (r ** 2), 'кв.од.'),
                    'Довжина': ('Довжина кола = 2 * π * Радіус', lambda r: 2 * 3.14 * r, 'од.'),
                    'Діаметр': ('Діаметр кола = 2 * Радіус', lambda r: 2 * r, 'од.')
                },
                'input_prompt': 'Введіть радіус кола: '
            },
            'Трикутник': {
                'formulas': {
                    'Площа': ('Площа трикутника = (Основа * Висота) / 2', lambda b, h: (b * h) / 2, 'кв.од.'),
                    'Периметр': (
                        'Периметр трикутника = Сторона1 + Сторона2 + Сторона3', lambda a, b, c: a + b + c, 'од.'),
                    'Півпериметр': (
                        'Півпериметр трикутника = (Сторона1 + Сторона2 + Сторона3) / 2',
                        lambda a, b, c: (a + b + c) / 2,
                        'од.')
                },
                'input_prompt': 'Введіть значення: '
            },
            'Квадрат': {
                'formulas': {
                    'Площа': ('Площа квадрата = Сторона ^ 2', lambda s: s ** 2, 'кв.од.'),
                    'Периметр': ('Периметр квадрата = 4 * Сторона', lambda s: 4 * s, 'од.'),
                    'Діагональ': ('Діагональ квадрата = Сторона * √2', lambda s: s * (2 ** 0.5), 'од.')
                },
                'input_prompt': 'Введіть значення сторони квадрата: '
            }
        }

        print('Доступні фігури: Коло, Трикутник, Квадрат')

        figure = input('Виберіть фігуру: ')

        if figure in figures:
            figure_data = figures[figure]
            formulas = figure_data['formulas']

            print(f'Доступні формули для {figure}:')
            for formula in formulas:
                print(f' - {formula}')

            formula_choice = input('Виберіть формулу: ')

            if formula_choice in formulas:
                formula_text, formula_func, unit_of_measurement = formulas[formula_choice]
                print('Формула:', formula_text)

                values = []
                for i in range(formula_func.__code__.co_argcount):
                    value = float(input(f'{figure_data["input_prompt"]} {formula_text.split()[i + 3]}: '))
                    values.append(value)

                result = formula_func(*values)
                print('Результат:', result, unit_of_measurement)
            else:
                print('Невідома формула')
        else:
            print('Невідома фігура')
