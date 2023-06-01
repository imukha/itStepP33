'''f1 = open('D:\\STEP_IT\\files\\myfile.txt', 'r')
s1 = f1.readline()
print(s1)
s2 = f1.readline()
print(s2)'''
'''
f1 = open('D:\\STEP_IT\\files\\myfile.txt', 'r')
print(f1.read(5))
print(f1.read(6))
print(f1.read())
'''
'''
f1 = open('D:\\STEP_IT\\files\\myfile.txt', 'r')
lines = f1.readlines()
print(lines)
'''

'''f1 = open('D:\\STEP_IT\\files\\myfile.txt', 'r')
for line in f1:
    print(line)
'''
'''
f2 = open('D:\\STEP_IT\\files\\myfile2.txt', 'w')
n = f2.write('Some text\nSome text2')
'''
'''import random

i = 0
spysok = []
while i < 30:
    chislo = random.randint(0, 1001)
    spysok += [chislo]
    i += 1
print(spysok)
f = open('D:\\STEP_IT\\files\\spysok.txt', 'w')
s = str(len(spysok))
f.write(s + '\n')
for i in spysok:
    s = str(i)
    f.write(s + ' ')
f.close()'''

'''f = open('D:\\STEP_IT\\files\\spysok.txt', 'r')
line = f.readline()
print(line)'''

'''srysok_txt = ['dasd', 'sdfs', 'sdfsd', 'erg']
f = open('D:\\STEP_IT\\files\\spysok.txt', 'w')

for line in srysok_txt:
    f.write(line + '\n')

f.close()
'''

'''slovnyk = {1: 'Mon', 2: 'Mon2', 3: 'Mon3', 4: 'Mon4', 5: 'Mon5'}
f = open('D:\\STEP_IT\\files\\spysok.txt', 'w')
for item in slovnyk:
    s = str(item)
    s += ':'
    s += slovnyk.get(item)
    s += '\n'
    f.write(s)

f.close()myfile
'''
'''f1 = open('D:\\STEP_IT\\files\\myfile.txt', 'r')
count = 0
s = f1.readline()
while s != '':
    s = f1.readline()
    count += 1
print(count)'''

'''f2 = open('D:\\STEP_IT\\files\\myfile2.txt', 'r')
spysok = f2.readline()
count = len(spysok)
print(count)
'''
'''
f3 = open('D:\\STEP_IT\\files\\myfile2.txt', 'r')
s = input('Введіть текст: ')
pos = 2
spysok = f3.readlines()
if (pos >= 0) and (pos < len(spysok)):
    if (pos == len(spysok) - 1):
        spysok[pos] = s
    else:
        spysok[pos] = s + '\n'
f3.close()
f3 = open('D:\\STEP_IT\\files\\myfile2.txt', 'w')
for line in spysok:
    f3.write(line)
f3.close()'''
'''
pos = int(input('pos='))
f = open('D:\\STEP_IT\\files\\myfile2.txt', 'r')
spysok = f.readlines()
if (pos >= 0) and (pos < len(spysok)):
    i = pos
    while i < len(spysok) - 1:
        spysok[i] = spysok[i + 1]
        i += 1
    spysok = spysok[:-1]
f.close()
f = open('D:\\STEP_IT\\files\\myfile2.txt', 'w')
for line in spysok:
    f.write(line)
f.close()'''
'''
f1 = open('D:\\STEP_IT\\files\\myfile.txt', 'r')
f2 = open('D:\\STEP_IT\\files\\myfile2.txt', 'r')

spysok1 = f1.readlines()
spysok2 = f2.readlines()
spysok3 = spysok1 + ['\n\n'] + spysok2

f1.close()
f2.close()

f3 = f2 = open('D:\\STEP_IT\\files\\file3.txt', 'w')
for i in spysok3:
    f3.write(i)
f3.close()

'''

while True:
    print("Меню:")
    print("1. Створити новий документ")
    print("2. Відредагувати документ")
    print("3. Об'єднати два документи")
    print("4. Вийти")

    choice = input("Виберіть опцію (1-4): ")

    if choice == "1":
        filename = input("Введіть назву файлу: ")
        with open(f"{filename}.txt", "w") as file:
            print(f"Файл {filename}.txt створено.")
    elif choice == "2":
        filename = input("Введіть назву файлу, який потрібно відредагувати: ")
        try:
            with open(f"{filename}.txt", "a+") as file:
                file.seek(0)
                lines = file.readlines()
                print("Зміст файлу:")
                for i, line in enumerate(lines):
                    print(f"{i + 1}. {line.rstrip()}")

                edit_choice = input("Оберіть дію:\n1 - Додати\n2 - Замінити\n3 - Видалити\n--> ")

                if edit_choice == "1":
                    new_line = input("Введіть новий рядок: ")
                    file.write(new_line + "\n")
                    print("Рядок додано успішно.")

                elif edit_choice == "2":
                    line_num = int(input("Введіть номер рядка, який потрібно замінити: "))
                    if line_num <= len(lines):
                        new_line = input("Введіть новий рядок: ")
                        lines[line_num - 1] = new_line + "\n"
                        file.seek(0)
                        file.writelines(lines)
                        file.truncate()
                        print("Рядок замінено успішно.")
                    else:
                        print("Недійсний номер рядка.")

                elif edit_choice == "3":
                    line_num = int(input("Введіть номер рядка, який потрібно видалити: "))
                    if line_num <= len(lines):
                        del lines[line_num - 1]
                        file.seek(0)
                        file.writelines(lines)
                        file.truncate()
                        print("Рядок видалено успішно.")
                    else:
                        print("Недійсний номер рядка.")

                else:
                    print("Недійсний вибір.")
        except FileNotFoundError:
            print("Файл не знайдено.")
    elif choice == "3":
        file1 = input("Введіть назву першого файлу: ")
        file2 = input("Введіть назву другого файлу: ")
        try:
            with open(f"{file1}.txt", "r") as f1, open(f"{file2}.txt", "r") as f2:
                content1 = f1.read()
                content2 = f2.read()

            merged_content = content1 + content2

            merged_filename = input("Введіть назву нового файлу (об'єднаного): ")
            with open(f"{merged_filename}.txt", "w") as merged_file:
                merged_file.write(merged_content)

            print(f"Файли {file1}.txt і {file2}.txt об'єднано в {merged_filename}.txt.")
        except FileNotFoundError:
            print("Один або обидва з файлів не знайдено.")
    elif choice == "4":
        break
    else:
        print("Недійсний вибір. Спробуйте ще раз.")
