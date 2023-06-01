while True:
    print('\nОберіть номер завдання:')
    print('1 - Завдання №1')
    print('2 - Завдання №2')
    print('3 - Завдання №3')
    print('4 - Завдання №4')
    print('5 - Завдання №5')
    print('6 - Завдання №6')
    choice = input('Ваш вибір: ')

    if choice == '1':
        # Завдання №1

        def multiply_list(lst):
            result = 1
            for num in lst:
                result *= num
            return result


        # виклику функції
        numbers = input("Введіть список цілих чисел через кому: ").split(",")
        numbers = [int(num) for num in numbers]
        product = multiply_list(numbers)
        print(f"Добуток елементів списку: {product}")

    elif choice == '2':
        # Завдання №2
        def find_min(lst):
            min_num = lst[0]
            for num in lst:
                if num < min_num:
                    min_num = num
            return min_num


        #  виклику функції
        numbers = input("Введіть список цілих чисел через кому: ").split(",")
        numbers = [int(num) for num in numbers]
        min_num = find_min(numbers)
        print(f"Мінімальний елемент списку: {min_num}")

    elif choice == '3':
        # Завдання №3
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True


        def count_primes(lst):
            count = 0
            for num in lst:
                if is_prime(num):
                    count += 1
            return count


        # виклику функції
        numbers = input("Введіть список цілих чисел через кому: ").split(",")
        numbers = [int(num) for num in numbers]
        prime_count = count_primes(numbers)
        print(f"Кількість простих чисел у списку: {prime_count}")

    elif choice == '4':
        # Завдання №4

        def remove_value(lst, value):
            count = 0
            for i in lst:
                if i == value:
                    lst.remove(i)
                    count += 1
            return count


        # виклику функції
        numbers = input("Введіть список цілих чисел через кому: ").split(",")
        numbers = [int(num) for num in numbers]
        value = int(input("Введіть значення, яке потрібно видалити: "))
        removed_count = remove_value(numbers, value)
        print(f"Кількість видалених елементів: {removed_count}")
        print(f"Змінений список: {numbers}")

    elif choice == '5':
        # Завдання №5

        def merge_lists(lst1, lst2):

            merged_list = lst1 + lst2
            return merged_list


        # виклику функції
        list1 = input("Введіть перший список цілих чисел через кому: ").split(",")
        list1 = [int(num) for num in list1]
        list2 = input("Введіть другий список цілих чисел через кому: ").split(",")
        list2 = [int(num) for num in list2]
        merged_list = merge_lists(list1, list2)
        print(f"Об'єднаний список: {merged_list}")

    elif choice == '6':
        # Завдання №6

        def calculate_powers(lst, power):
            powered_list = [num ** power for num in lst]
            return powered_list


        #  виклику функції
        lst = input("Введіть список цілих чисел через кому: ").split(",")
        lst = [int(num) for num in lst]
        power = int(input("Введіть степінь, до якої потрібно підняти кожен елемент списку: "))
        powered_lst = calculate_powers(lst, power)
        print(f"Новий список з елементами, піднесеними до степеня {power}: {powered_lst}")
    else:
        print('Не правильний ввід, спробуйте ще раз!👇🏻👇🏻👇🏻')
