while True:
    print("\nМеню:")
    print("1. Завдання №1 'Відомі баскетболісти'")
    print("2. Завдання №2 'Англо-французький словник'")
    print("3. Завдання №3 'Фірма'")
    print("4. Завдання №4 'Книжкова колекція'")
    choice = input("Ваш вибір: ")

    # Завдання №1

    if choice == '1':
        # Створення словника з даними про баскедболістів
        basketball_players = {
            "LeBron James": {"height": "206 см", "age": "37 років", "phone": "555-1234"},
            "Kevin Durant": {"height": "211 см", "age": "33 роки", "phone": "555-5678"},
            "Stephen Curry": {"height": "191 см", "age": "33 роки", "phone": "555-9876"},
            "Kawhi Leonard": {"height": "201 см", "age": "30 років", "phone": "555-2468"}
        }

        while True:
            # Виведення меню опцій
            print("\nВиберіть опцію:")
            print("0. Вивести список баскетболістів")
            print("1. Додати нового баскетболіста")
            print("2. Видалити баскетболіста")
            print("3. Змінити дані про баскетболіста")
            print("4. Знайти баскетболіста")
            print("5. Вийти з програми")

            choice = input("Ваш вибір: ")

            # Виконання вибраної опції
            if choice == '0':
                if basketball_players:
                    print("Список баскетболістів:")
                    for name, data in basketball_players.items():
                        print(f"{name} - вік: {data['age']}, зріст: {data['height']}, телефон: {data['phone']}")
                else:
                    print("Список баскетболістів порожній.")

            elif choice == '1':
                name = input("Введіть ПІБ баскетболіста: ")
                height = input("Введіть зріст баскетболіста: ")
                age = input("Введіть вік баскетболіста: ")
                phone = input("Введіть номер телефону баскетболіста: ")
                basketball_players[name] = {"height": height, "age": age, "phone": phone}
                print("Дані збережено.")

            elif choice == '2':
                name = input("Введіть ПІБ баскетболіста, якого потрібно видалити: ")
                if name in basketball_players:
                    del basketball_players[name]
                    print("Баскетболіста видалено.")
                else:
                    print("Такого баскетболіста не знайдено.")

            elif choice == '3':
                name = input("Введіть ПІБ баскетболіста, якого потрібно змінити: ")
                if name in basketball_players:
                    height = input("Введіть новий зріст баскетболіста: ")
                    age = input("Введіть новий вік баскетболіста: ")
                    phone = input("Введіть новий номер телефону баскетболіста: ")
                    basketball_players[name] = {"height": height, "age": age, "phone": phone}
                    print("Дані збережено.")
                else:
                    print("Такого баскетболіста не знайдено.")

            elif choice == '4':
                name = input("Введіть ПІБ баскетболіста: ")
                if name in basketball_players:
                    data = basketball_players[name]
                    print(f"{name} - вік: {data['age']}, зріст: {data['height']}, телефон: {data['phone']}")
                else:
                    print(f"Баскетболіст '{name}' не знайдений.")

            elif choice == '5':
                print("Дякуємо за користування програмою!")
                break

    # Завдання №2

    elif choice == '2':
        # Створення словника з даними слово та його переклад
        dictionary = {"dog": "chienne", "cat": "chatte", "snake": "serpent", "home": "maison", "men": "Hommes"}

        # Виведення меню опцій
        while True:
            print("\nМеню:")
            print("1. Показати словник")
            print("2. Перекласти слово")
            print("3. Додати нове слово")
            print("4. Вийти з програми")
            choice = input("Ваш вибір: ")

            # Виконання вибраної опції
            if choice == "1":
                print("Словник:")
                for word in dictionary:
                    print(f"{word} - {dictionary[word]}")

            elif choice == "2":
                word = input("Яке слово потрібно перекласти? ")
                if word in dictionary:
                    print(f"Переклад слова '{word}': {dictionary[word]}")
                else:
                    answer = input(f"Слово '{word}' не знайдено. Бажаєте додати його до словника? (так/ні) ")
                    if answer == "так":
                        translation = input(f"Який переклад слова '{word}'? ")
                        dictionary[word] = translation
                        print(f"Слово '{word}' успішно додано до словника з перекладом '{translation}'")
                    else:
                        print(f"Переклад слова '{word}' не знайдено")

            elif choice == "3":
                word = input("Яке слово потрібно додати до словника? ")
                if word in dictionary:
                    print(f"Слово '{word}' вже є у словнику з перекладом '{dictionary[word]}'")
                else:
                    translation = input(f"Який переклад слова '{word}'? ")
                    dictionary[word] = translation
                    print(f"Слово '{word}' успішно додано до словника з перекладом '{translation}'")

            elif choice == "4":
                print("До побачення!")
                break
            else:
                print("Неправильний вибір. Спробуйте ще раз.")

        # Завдання №3

    elif choice == '3':
        # Створення словника з даними про працівників фірми
        list_of_employees = {
            "Mukhaid Ivan": {"phone": "0934646138", "email": "mukhaid.corp@gmail.com", "position": "Директор",
                             "office number": "1", "Skype": "mukhaid.sk"},
            "Wer wer": {"phone": "0992992019", "email": "wer.corp@gmail.com", "position": "Секретар",
                        "office number": "2", "Skype": "wer.sk"},
            "Gladish Tatyana": {"phone": "722457764", "email": "gladish.corp@gmail.com", "position": "Бухгалтер",
                                "office number": "3", "Skype": "gladish.sk"},
            "Fastovech Olena": {"phone": "0662342323", "email": "fastovech.corp@gmail.com", "position": "Економіст",
                                "office number": "4", "Skype": "fastovech.sk"}
        }

        while True:
            # Виведення меню опцій

            print("\nВиберіть опцію:")
            print("0. Вивести список робітників")
            print("1. Додати нового робітника")
            print("2. Видалити робітника")
            print("3. Змінити дані про робітника")
            print("4. Знайти робітника")
            print("5. Вийти з програми")

            choice = input("Ваш вибір: ")

            # Виконання вибраної опції

            if choice == '0':
                if list_of_employees:
                    print("Список робітників:")
                    for name, data in list_of_employees.items():
                        print(f"{name} - телефон: {data['phone']}, email: {data['email']}, посада: {data['position']},"
                              f" номер кабінету: {data['office number']}, Skype: {data['Skype']}")
                else:
                    print("Список робітників порожній.")

            elif choice == '1':
                name = input("Введіть ПІБ робітника: ")
                phone = input("Введіть номер телефону робітника: ")
                email = input("Введіть email робітника: ")
                position = input("Введіть посаду робітника: ")
                office_number = input("Введіть номер кабінету робітника: ")
                Skype = input("Введіть Skype робітника: ")
                list_of_employees[name] = {"phone": phone, "email": email, "position": position,
                                           "office number": office_number, "Skype": Skype}
                print("Дані збережено.")

            elif choice == '2':
                name = input("Введіть ПІБ робітника, якого потрібно видалити: ")
                if name in list_of_employees:
                    del list_of_employees[name]
                    print("Робітника видалено.")
                else:
                    print("Такого робітника не знайдено.")

            elif choice == '3':
                name = input("Введіть ПІБ робітника, якого потрібно змінити: ")
                if name in list_of_employees:
                    phone = input("Введіть номер телефону робітника: ")
                    email = input("Введіть email робітника: ")
                    position = input("Введіть посаду робітника: ")
                    office_number = input("Введіть номер кабінету робітника: ")
                    Skype = input("Введіть Skype робітника: ")
                    list_of_employees[name] = {"phone": phone, "email": email, "position": position,
                                               "office number": office_number, "Skype": Skype}
                    print("Дані збережено.")
                else:
                    print("Такого робітника не знайдено.")

            elif choice == '4':
                name = input("Введіть ПІБ робітника: ")
                if name in list_of_employees:
                    data = list_of_employees[name]
                    print(f"{name} - телефон: {data['phone']}, email: {data['email']}, посада: {data['position']},"
                          f" номер кабінету: {data['office number']}, Skype: {data['Skype']}")
                else:
                    print(f"робітник {name} не знайдений.")

            elif choice == '5':
                print("Дякуємо за користування програмою!")
                break

    # Завдання №4
    elif choice == '4':
        # Створення словника з даними про книги
        book_collection = [
            {'автор': 'Леся Українка', 'назва книги': 'Лісова пісня', 'жанр': 'драма', 'рік випуску': 1911,
             'кількість сторінок': 192, 'видавництво': 'Київська старина'},
            {'автор': 'Іван Франко', 'назва книги': 'Захар Беркут', 'жанр': 'історичний роман', 'рік випуску': 1891,
             'кількість сторінок': 312, 'видавництво': 'Сучасність'},
            {'автор': 'Михайло Коцюбинський', 'назва книги': 'Тіні забутих предків', 'жанр': 'роман',
             'рік випуску': 1911,
             'кількість сторінок': 392, 'видавництво': 'Жовтень'},
            {'автор': 'Ольга Кобилянська', 'назва книги': 'Земля', 'жанр': 'драма', 'рік випуску': 1902,
             'кількість сторінок': 288, 'видавництво': 'Світ'},
            {'автор': 'Марко Вовчок', 'назва книги': 'Гарячий Яр', 'жанр': 'роман', 'рік випуску': 1878,
             'кількість сторінок': 240, 'видавництво': 'Київська старина'},
            {'автор': 'Ліна Костенко', 'назва книги': 'Маруся Чурай', 'жанр': 'роман', 'рік випуску': 1996,
             'кількість сторінок': 384, 'видавництво': 'Дніпро'},
            {'автор': 'Василь Стефаник', 'назва книги': 'Хіба ревуть воли, як ясла повні?', 'жанр': 'роман',
             'рік випуску': 1921,
             'кількість сторінок': 136, 'видавництво': 'Дніпро'},
            {'автор': 'Іван Нечуй-Левицький', 'назва книги': 'Кайдашева сім\'я', 'жанр': 'роман', 'рік випуску': 1898,
             'кількість сторінок': 240, 'видавництво': 'Сучасність'},
            {'автор': 'Олесь Гончар', 'назва книги': 'Собор', 'жанр': 'роман', 'рік випуску': 1968,
             'кількість сторінок': 576, 'видавництво': 'Дніпро'},
        ]

        while True:
            # Виведення меню опцій

            print("\nВиберіть опцію:")
            print("0. Вивести список книг")
            print("1. Додати нову книгу")
            print("2. Знайти книгу")
            # print("3. Змінити дані про книгу")
            # print("4. Знайти книгу")
            print("3. Вийти з програми")

            choice = input("Ваш вибір: ")

            # Виконання вибраної опції

            # "0. Вивести список книг"
            if choice == '0':
                if book_collection:
                    print("Список книг:")
                    for book in book_collection:
                        print(book)
                else:
                    print("Список робітників порожній.")

            # "1. Додати нову книгу"
            elif choice == '1':
                author = input("Введіть автора книги: ")
                book_title = input("Введіть назву книги: ")
                genre = input("Введіть жанр книги: ")
                year = int(input("Введіть рік випуску книги: "))
                pages = int(input("Введіть кількість сторінок в книзі: "))
                publishing_house = input("Введіть видавництво книги: ")
                new_book = {'автор': author, 'назва книги': book_title, 'жанр': genre, 'рік випуску': year,
                            'кількість сторінок': pages, 'видавництво': publishing_house}
                book_collection.append(new_book)
                print("Дані збережено.")

            # "2. Знайти книгу"
            elif choice == '2':
                keyName = input(
                    'Введіть назву категорії за якою будемо шукати книгу:\n1. Автор;\n2. Назва книги;\n3. Жанр;'
                    '\n4. Рік випуску;\n5. Кількість сторінок;\n6. Видавництво;\n>>> '
                )

                # Перетворюємо введення користувача у відповідну категорію
                if keyName == '1':
                    keyName = 'автор'
                elif keyName == '2':
                    keyName = 'назва книги'
                elif keyName == '3':
                    keyName = 'жанр'
                elif keyName == '4':
                    keyName = 'рік випуску'
                elif keyName == '5':
                    keyName = 'кількість сторінок'
                elif keyName == '6':
                    keyName = 'видавництво'
                else:
                    print('Ви ввели невірне значення!')

                keyValue = input('Введіть конкретні дані для пошуку: ')

                if keyName == 'рік випуску' and keyValue.isdigit():
                    # Перетворюємо рік випуску у числовий формат
                    keyValue = int(keyValue)
                elif keyName == 'кількість сторінок' and keyValue.isdigit():
                    # Перетворюємо кількість сторінок у числовий формат
                    keyValue = int(keyValue.lower())

                isElementFound = False

                for book in book_collection:
                    if isinstance(keyValue, str):
                        keyValue = keyValue.lower()
                    if isinstance(book.get(keyName), str):
                        book_value = book.get(keyName).lower()
                    else:
                        book_value = book.get(keyName)
                    if book_value == keyValue:
                        print('\nЕлемент знайдено:')

                        for key, value in book.items():
                            print('{}: {}'.format(key, value))
                        isElementFound = True

                        # Вибір дії зі знайденою книгою
                        choice = input(print(
                            'Оберіть дію: \n1. Видалити книгу.\n2. Змінити дані про книгу.'
                            '\n3. Повернутись в головне меню.\n>>>'))

                        # видалити книгу
                        if choice == '1':
                            delete_choice = input('Ви дійсно хочете видалити цю книгу? (так/ні) ')
                            if delete_choice == 'так':
                                book_collection.remove(book)
                                print('Книга успішно видалена!')
                            else:
                                print('Книга не була видалена.')

                        # Змінити дані про книгу
                        elif choice == '2':
                            update_choice = input('Ви дійсно хочете оновити дані про цю книгу? (так/ні) ')
                            if update_choice == 'так':
                                for key in book:
                                    new_value = input(f'Введіть нове значення для поля "{key}": ')
                                    book[key] = new_value
                                print('Дані про книгу успішно оновлені!')
                            else:
                                print('Дані про книгу не були оновлені.')
                        if not isElementFound:
                            print('Елемент не знайдено!')
                            # Вихід з пошуку
                        elif choice == '3':
                            print("Дякуємо за користування програмою!")
                            break

            elif choice == '3':
                print("Дякуємо за користування програмою!")
                break


    else:
        print("Неправильний вибір. Спробуйте ще раз.")
