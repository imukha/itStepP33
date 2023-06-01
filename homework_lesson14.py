import os

files = {}

while True:
    print("Меню:")
    print("1. Створити файл")
    print("2. Відредагувати файл")
    print("3. Об'єднати два файли")
    print("4. Вивести зміст файлу")
    print("5. Видалити файл")
    print("6. Вийти")

    choice = input("Виберіть опцію (1-6): ")

    if choice == "1":
        filename = input("Введіть назву файлу: ")
        directory = input("Введіть шлях до директорії (або залиште порожнім для поточної директорії): ")
        if directory:
            if not os.path.isdir(directory):
                print("Помилка: директорія не існує.")
                continue

            file_path = os.path.join(directory, f"{filename}.txt")
        else:
            file_path = f"{filename}.txt"

        with open(file_path, "a") as file:
            print(f"Файл {filename}.txt створено.")
            file_content = ""
            while True:
                line = input("Введіть рядок тексту (або Enter - закінчити): ")
                if line == "":
                    break
                file_content += line + "\n"

            file.write(file_content)
            print("Рядки збережено успішно.")

        try:
            with open(file_path, "r") as file:
                print(f"Зміст файлу {filename}.txt:")
                print(file.read())
        except FileNotFoundError:
            print("Помилка: файл не знайдено.")



    elif choice == "2":

        filename = input("Введіть назву файлу, який потрібно відредагувати: ")
        directory = input("Введіть шлях до директорії (або залиште порожнім для поточної директорії): ")
        if directory:
            file_path = os.path.join(directory, f"{filename}.txt")
        else:
            file_path = f"{filename}.txt"

        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                print(f"Зміст файлу {filename}.txt:")
                for i, line in enumerate(lines):
                    print(f"{i + 1}. {line.strip()}")
            if not lines:
                print("Файл порожній. Введіть дані в перший рядок.")
                new_line = input("Введіть новий рядок: ")
                lines.append(new_line + "\n")

            else:
                line_num = int(input("Введіть номер рядка, який потрібно змінити: "))
                if 1 <= line_num <= len(lines):
                    new_line = input("Введіть новий рядок: ")
                    lines[line_num - 1] = new_line + "\n"
                    print("Рядок змінено успішно.")
                else:
                    print("Недійсний номер рядка.")

            with open(file_path, "w") as file:
                file.writelines(lines)
            print(f"Зміст файлу {filename}.txt:")
            with open(file_path, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("Файл не знайдено.")

        except ValueError:
            print("Недійсний номер рядка.")

    elif choice == "3":
        file1 = input("Введіть назву першого файлу: ")
        file2 = input("Введіть назву другого файлу: ")
        directory = input("Введіть шлях до директорії (або залиште порожнім для поточної директорії): ")
        if directory:
            file1_path = os.path.join(directory, f"{file1}.txt")
            file2_path = os.path.join(directory, f"{file2}.txt")
        else:
            file1_path = f"{file1}.txt"
            file2_path = f"{file2}.txt"

        try:
            with open(file1_path, "r") as f1, open(file2_path, "r") as f2:
                content1 = f1.read()
                content2 = f2.read()

            merged_filename = input("Введіть назву нового файлу (об'єднаного): ")
            merged_file_path = os.path.join(directory, f"{merged_filename}.txt")
            with open(merged_file_path, "w") as merged_file:
                merged_file.write(content1 + content2)

            print(f"Файли {file1}.txt і {file2}.txt об'єднано в {merged_filename}.txt.")

            try:
                with open(merged_file_path, "r") as file:
                    print(f"Зміст файлу {merged_filename}.txt:")
                    print(file.read())
            except FileNotFoundError:
                print("Помилка: файл не знайдено.")

        except FileNotFoundError:
            print("Один або обидва з файлів не знайдено за вказаною директорією.")



    elif choice == "4":
        filename = input("Введіть назву файлу, який потрібно переглянути: ")
        directory = input("Введіть шлях до директорії (або залиште порожнім для поточної директорії): ")
        if directory:
            file_path = os.path.join(directory, f"{filename}.txt")
        else:
            file_path = f"{filename}.txt"

        try:
            with open(file_path, "r") as file:
                print(f"Зміст файлу {filename}.txt:")
                print(file.read())
        except FileNotFoundError:
            print("Помилка: файл не знайдено.")

    elif choice == "5":
        filename = input("Введіть назву файлу, який потрібно видалити: ")
        directory = input("Введіть шлях до директорії (або залиште порожнім для поточної директорії): ")
        if directory:
            file_path = os.path.join(directory, f"{filename}.txt")
        else:
            file_path = f"{filename}.txt"

        try:
            os.remove(file_path)
            print(f"Файл {filename}.txt видалено.")
        except FileNotFoundError:
            print("Помилка: файл не знайдено.")

    elif choice == "6":
        break

    else:
        print("Недійсний вибір. Спробуйте ще раз.")
