while True:

    print('\n1 - Завдання №1')
    print('2 - Завдання №2')
    print('3 - Завдання №3')
    print('4 - Завдання №4')
    print('5 - Завдання №5')
    print('6 - Завдання №6')
    print('7 - Завдання №7')
    choice = input('Оберіть номер завдання: ')

    # Завдання №1

    if choice == '1':
        print('Функція, яка виводить на екран форматований текст:\n')


        def print_quote():
            print('“Don’t compare yourself with anyone in this world…')
            print('if you do so, you are insulting yourself.”')
            print('                                         Bill Gates')


        print_quote()



    # Завдання №2

    elif choice == '2':
        print('Функція, яка приймає два числа як параметр і відображає усі парні числа між ними.\n')

        start = int(input('Введіть перше число: '))
        end = int(input('Введіть друге число: '))


        def display_even_numbers(start, end):
            for num in range(start, end + 1):
                if num % 2 == 0:
                    print(num)


        print('Всі парні числа в заданому діапазоні:')
        display_even_numbers(start, end)



    # Завдання №3

    elif choice == '3':
        print('Функція, яка відображає порожній або заповнений квадрат із певним символом. \n')


        def display_square():
            length = int(input("Введіть довжину сторони квадрата: "))
            symbol = input("Введіть символ для квадрата: ")
            is_filled = input("Чи заповнений квадрат? (введіть True або False): ").lower() == "true"

            if is_filled:
                for i in range(length):
                    print(symbol * length)
            else:
                print(symbol * length)
                for i in range(length - 2):
                    print(symbol + ' ' * (length - 2) + symbol)
                print(symbol * length)


        display_square()

    # Завдання №4

    elif choice == '4':
        print('Функція, яка повертає мінімальне значення з п’яти чисел.\n')


        def find_min(*numbers):
            return min(numbers)


        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        c = float(input("Введіть третє число: "))
        d = float(input("Введіть четверте число: "))
        e = float(input("Введіть п'яте число: "))

        min_num = find_min(a, b, c, d, e)
        print("Мінімальне число: ", min_num)

        # Завдання №5

    elif choice == '5':
        print('Функція, яка повертає добуток чисел у зазначеному діапазоні.\n')


        def multiply_in_range(num1, num2):
            # Перевіряємо, чи межі діапазону переплутані
            if num1 > num2:
                num1, num2 = num2, num1
            product = 1
            # Обчислюємо добуток чисел у діапазоні
            for num in range(num1, num2 + 1):
                product *= num
            # Повертаємо добуток
            return product


        # використання функції
        num1 = int(input("Введіть перше число: "))
        num2 = int(input("Введіть друге число: "))
        result = multiply_in_range(num1, num2)
        print(f"Добуток чисел у діапазоні від {num1} до {num2} дорівнює {result}")


    # Завдання №6

    elif choice == '6':
        print('Функція, яка підраховує кількість цифр у числі.\n')


        def count_digits(number):
            count = 0
            while number != 0:
                count += 1
                number //= 10
            return count


        # використання функції
        number = int(input("Введіть число: "))
        result = count_digits(number)
        print(f"Кількість цифр у числі {number} дорівнює {result}")


    # Завдання №7

    elif choice == '7':
        print('Функція, яка перевіряє число на паліндром.\n')


        def is_palindrome(number):
            # перетворюємо число на рядок (строку) і зберігаємо його в змінній
            number_str = str(number)
            # порівнюємо рядок з його оберненим варіантом
            if number_str == number_str[::-1]:
                return True
            else:
                return False


        # використання функції
        number = int(input("Введіть число: "))
        result = is_palindrome(number)
        if result:
            print(f"Число {number} є паліндромом.")
        else:
            print(f"Число {number} НЕ є паліндромом.")

    else:
        print('Не правильний вибір, спробуйте ще раз.\n')
