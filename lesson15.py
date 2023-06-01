import datetime

'''date_time = datetime.datetime(2023, 5, 23, hour=19, minute=24, second=23, microsecond=585)
print(f'objekt datetime - {date_time}')
print(f'type-{type(date_time)}')'''

'''date_time = datetime.datetime(2023, 5, 23, hour=19, minute=24, second=23, microsecond=585)
print(f'method data() -{date_time.date()}\n type - {type(date_time.date())}')
print(f'{date_time.time()}\n type - {type(date_time.date())}')
date_1 = datetime.date(2021, 9, 24)
time_1 = datetime.time(5, 8, 48)
print(date_1)
print(time_1)
date_and_time = datetime.datetime.combine(date_1, time_1)
print(f'datetime = {date_and_time}, type date = {type(date_and_time)}')

print(f'new date = {date_1.replace(2022)}')
print(f'old date = {date_1}')'''
'''
date_now = datetime.datetime.now()
date_today = datetime.datetime.today()
date_date = datetime.date.today()
print(date_now)
print(date_today)
print(date_date)

print(f'time now = {date_now.time()}')

date_for_now = datetime.datetime.now()
print(f'weekday() = {date_for_now.weekday()}')
print(f'isoweekday() = {date_for_now.isoweekday()}')
'''

'''date_now = datetime.datetime.now()
print(date_now.strftime('%d.%m.%Y %H:%M %A %B %U %W'))

date_str = '28/09/2021 11:20'
date_str_res = datetime.datetime.strptime(date_str, '%d/%m/%Y %H:%M')
print(date_str_res)'''

'''date_now = datetime.datetime.now()
date = datetime.datetime(day=20, month=8, year=2020)
print(date_now - date)'''

'''date_now = datetime.datetime.now()
print(date_now)
delta = datetime.timedelta(days=20, hours=8, weeks=4)
print(delta)
a = date_now + delta
print(a.strftime('%d.%m.%Y %H:%M'))
'''

import datetime

while True:

    print("\nВиберіть опцію:")
    print("1) Отримати поточну дату.")
    print("2) Дізнатися день тижня.")
    print("3) Дізнатися поточний час.")
    print("4) Розрахувати кількість днів до вказаної дати.")
    print("5) Розрахувати дату через певну кількість днів.")
    choice = input("Ваш вибір (1-5): ")

    if choice == "1":
        current_date = datetime.date.today()
        print("Поточна дата:", current_date)
    elif choice == "2":
        current_weekday = datetime.date.today().strftime("%A")
        print("День тижня:", current_weekday)
    elif choice == "3":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Поточний час:", current_time)
    elif choice == "4":
        input_date = input("Введіть дату (у форматі РРРР-ММ-ДД): ")
        target_date = datetime.datetime.strptime(input_date, "%Y-%m-%d").date()
        current_date = datetime.date.today()
        days_until = (target_date - current_date).days
        print("Кількість днів до вказаної дати:", days_until)
    elif choice == "5":
        input_days = int(input("Введіть кількість днів: "))
        current_date = datetime.date.today()
        future_date = current_date + datetime.timedelta(days=input_days)
        print("Дата через", input_days, "днів:", future_date)
    else:
        print("Невірний вибір.")

import os

'''path = 'C:\\Windows\\Web'
for path, dirnames, filename in os.walk(path):
    print(path)
    print(dirnames)
    print(filename)

cor = 'C:\\'
dir1 = input('enter folder')
dir2 = input('enter folder')
path = os.path.join(cor, dir1, dir2)
for path, dirnames, filename in os.walk(path):
    print(path)
'''
