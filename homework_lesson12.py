import tkinter as tk
import re


def authenticate():
    username = username_entry.get()
    password = password_entry.get()

    # Список імен одногрупників
    group_names = {
        "Іван": {"вік": 25, "зріст": 180, "стаж роботи": 3},
        "Дмитро": {"вік": 28, "зріст": 175, "стаж роботи": 5},
        "Олексій": {"вік": 23, "зріст": 170, "стаж роботи": 2}
    }

    # Словник з паролями кожного імені
    passwords = {
        "Іван": "11111111",
        "Дмитро": "22222222",
        "Олексій": "33333333"
    }

    if username in group_names:
        if password == passwords.get(username):
            success_window = tk.Toplevel(root)
            success_window.title("Успішний вхід")
            success_window.geometry('400x100+180+150')

            message_label = tk.Label(success_window, text=f"Вхід успішний. Ласкаво просимо, {username}!",
                                     font=('Arial', 14), fg="green")
            ok_button = tk.Button(success_window, text="ОК", font=('Arial', 12), width=20,
                                  command=success_window.destroy)

            message_label.pack()
            ok_button.pack()

            # Отримання інформації про введене ім'я
            user_info = group_names.get(username)
            info_label.config(text=f"Інформація про {username}: "
                                   f"\nвік - {user_info['вік']}, "
                                   f"\nзріст - {user_info['зріст']}, "
                                   f"\nстаж роботи - {user_info['стаж роботи']}")
        else:
            error_label.config(text="Неправильний пароль", fg="red")
    else:
        error_label.config(text="Такого користувача не існує!", fg="red")


def close_window():
    root.destroy()


root = tk.Tk()
root.geometry('350x300+150+100')
root.title("Вхід")

username_label = tk.Label(root, text="Ім'я користувача:", font=('Arial', 14))
username_entry = tk.Entry(root, font=('Arial', 12), width=20)
password_label = tk.Label(root, text="Пароль:", font=('Arial', 14))
password_entry = tk.Entry(root, show="*", font=('Arial', 12), width=20)
authenticate_button = tk.Button(root, text="Увійти", font=('Arial', 12), command=authenticate)
close_button = tk.Button(root, text="Зареєструватись", font=('Arial', 12), command=close_window)
error_label = tk.Label(root, font=('Arial', 14), fg="red")
info_label = tk.Label(root, font=('Arial', 14))

username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
authenticate_button.pack()
close_button.pack()
error_label.pack()
info_label.pack()

root.mainloop()


def validate_input():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Перевірка правильності введеного імені
    if not re.match(r"^\w{3,20}$", username):
        error_label.config(text="Неправильне ім'я користувача", fg="red")
        username_entry.config(bg='red')
        return False

    # Перевірка правильності введеного емейлу
    if not re.match(r"^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$", email):
        error_label.config(text="Неправильний формат емейлу", fg="red")
        email_entry.config(bg='red')
        return False

    # Перевірка правильності введеного паролю
    if not re.match(r"^\w{8,16}$", password):
        error_label.config(text="Неправильний формат паролю", fg="red")
        password_entry.config(bg='red')
        return False

    if password == confirm_password:
        # Додаткова логіка реєстрації користувача
        # Створення нового вікна для сповіщення про успішну реєстрацію
        success_window = tk.Toplevel(root2)
        success_window.title("Успішна реєстрація")
        success_window.geometry('300x100+180+150')

        # Створення віджетів на новому вікні
        message_label = tk.Label(success_window, text="Реєстрація пройшла успішно!", font=('Arial', 14), fg="green")
        ok_button = tk.Button(success_window, text="ОК", font=('Arial', 12), width=20, command=success_window.destroy)

        # Розташування віджетів на новому вікні
        message_label.pack()
        ok_button.pack()
    else:
        # Повідомлення про невідповідність паролів
        error_label.config(text="Паролі не співпадають", fg="red")
        confirm_password_entry.config(bg='red')


root2 = tk.Tk()
root2.geometry('350x300+150+100')
root2.title("Реєстрація")

# Створення віджетів
username_label = tk.Label(root2, text="Ім'я користувача:", font=('Arial', 14))
email_label = tk.Label(root2, text="Ваш email:", font=('Arial', 14))
password_label = tk.Label(root2, text="Пароль:", font=('Arial', 14))
confirm_password_label = tk.Label(root2, text="Повторіть пароль:", font=('Arial', 14))
username_entry = tk.Entry(root2, font=('Arial', 12), width=20)
email_entry = tk.Entry(root2, font=('Arial', 12), width=20)
password_entry = tk.Entry(root2, show="*", font=('Arial', 12), width=20)
confirm_password_entry = tk.Entry(root2, show="*", font=('Arial', 12), width=20)
register_button = tk.Button(root2, text="Зареєструватись", font=('Arial', 12), command=validate_input)
error_label = tk.Label(root2, font=('Arial', 14), fg="red")

# Розташування віджетів на формі
username_label.pack()
username_entry.pack()
email_label.pack()
email_entry.pack()
password_label.pack()
password_entry.pack()
confirm_password_label.pack()
confirm_password_entry.pack()
register_button.pack()
error_label.pack()

root2.mainloop()
