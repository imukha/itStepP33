import tkinter as tk
import re

rech = 'По всім питанням писати на почту qwerty_1@gmail.com, або на newadres@ukr.net, або на itstep@outluc.com'
login_patter = re.compile(r"^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$")
password_pattern = re.compile(r'^\w{8,16}$')
user_pattern = re.compile(r"^\w{4,8}@[a-z]{2,10}\.[a-z]{2,6}$")

login_patter1 = re.compile(r"^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$")
password_pattern1 = re.compile(r'^\w{8,16}$')
# user_pattern1 = re.compile(r"^\w{4,8}@[a-z]{2,10}\.[a-z]{2,6}$")

# ^ - початок рядка
# $ - рядок закінчився
root1 = tk.Tk()
root = tk.Tk()

root.geometry('600x450+950+500')
root1.geometry('600x450+300+500')

root.resizable(False, False)
root1.resizable(False, False)


# root1.configure(background='#020357')


def logining():
    login = login_entry.get()
    password = password_entry.get()
    if login_patter.search(login):
        if password_pattern.search(password):
            login_entry.config(bg='#15edc9')
            password_entry.config(bg='#15edc9')
        else:
            login_entry.config(bg='#15edc9')
            password_entry.config(bg='red')
    else:
        login_entry.config(bg='red')
        password_entry.config(bg='red')


login_lable = tk.Label(root, text='Login:', font=('Arial', 14), padx=50, fg='red')
password_lable = tk.Label(root, text='Password:', font=('Arial', 14), padx=35, fg='red')

login_entry = tk.Entry(root, font=('Arial', 12), width=20)  # , background='blue'
password_entry = tk.Entry(root, font=('Arial', 12), width=20, show='*')  # , background='blue'

login_button = tk.Button(root, text='LOGIN', font=('Arial', 16), width=12, command=logining)

root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=250)
root.grid_rowconfigure(0, minsize=90)
root.grid_rowconfigure(1, minsize=90)
login_button.grid(columnspan=2)

login_lable.grid(column=0, row=0, sticky='w')
password_lable.grid(column=0, row=1, sticky='w')

login_entry.grid(column=1, row=0, sticky='w')
password_entry.grid(column=1, row=1, sticky='w')

login_button.grid(column=1, row=2)


def logining_n():
    login = login_entry1.get()
    password = password_entry1.get()
    if login_patter1.search(login):
        if password_pattern1.search(password):
            login_entry1.config(bg='#15edc9')
            password_entry1.config(bg='#15edc9')
            user_entry1.config(bg='#15edc9')
        else:
            login_entry1.config(bg='#15edc9')
            password_entry1.config(bg='red')
            user_entry1.config(bg='red')
    else:
        login_entry1.config(bg='red')
        password_entry1.config(bg='red')
        user_entry1.config(bg='red')


login_lable1 = tk.Label(root1, text='Login:', font=('Arial', 14), padx=50, fg='red')
password_lable1 = tk.Label(root1, text='Password:', font=('Arial', 14), padx=35, fg='red')
user_lable1 = tk.Label(root1, text='User:', font=('Arial', 14), padx=35, fg='red')

login_entry1 = tk.Entry(root1, font=('Arial', 12), width=20)  # , background='blue'
password_entry1 = tk.Entry(root1, font=('Arial', 12), width=20, show='*')  # , background='blue'
user_entry1 = tk.Entry(root1, font=('Arial', 12), width=20, show='*')

login_button1 = tk.Button(root1, text='LOGIN', font=('Arial', 16), width=12, command=logining_n)

root1.grid_columnconfigure(0, minsize=150)
root1.grid_columnconfigure(1, minsize=250)
root1.grid_rowconfigure(0, minsize=90)
root1.grid_rowconfigure(1, minsize=90)
login_button1.grid(columnspan=2)

login_lable1.grid(column=0, row=0, sticky='w')
password_lable1.grid(column=0, row=1, sticky='w')
user_lable1.grid(column=0, row=2, sticky='w')

login_entry1.grid(column=1, row=0, sticky='w')
password_entry1.grid(column=1, row=1, sticky='w')
user_entry1.grid(column=1, row=2, sticky='w')

login_button1.grid(column=0, row=3)

root1.mainloop()
