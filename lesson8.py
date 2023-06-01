'''myDict = {'key1': 1, 'key2': 2, 'key3': True, }
myDict2 = {1: 'student', 2: 'admin'}
print(myDict)
print(myDict2)

A = {}
print('A = ', A)

B = {1: 'Mon', 2: 'Tue', 3: 'Wes', 4: 'Thu'}
print(B)
print(B[2])

slovnyk = {'Pi': 3.1415, 'Exp': 1.71}
print(slovnyk)
print(slovnyk['Exp'])

slovnyk_nabir = {'slovnyk1': [1, 2, 'Hello'], }
print(slovnyk_nabir)
print(slovnyk_nabir['slovnyk1'][1])
'''

'''pystiy_slovnyk = dict()
print(pystiy_slovnyk)

weak = dict(Monday=1, Tuesday=2)
print(weak)

Days = [1, 2, 3, 4]
days_n = ['Mon', 'Tue', 'Wes', 'Thu']
all_d = dict(zip(Days, days_n))
print(all_d)

pairs_d = dict([(1, 'Wintetr'), (2, 'Summer'), (3, 'Spring')])
print(pairs_d)'''

'''weak = dict(Monday=1, Tuesday=2)
value = weak['Monday']
print(value)'''

'''slovnyk = {1: 'Python', 2: 'C++', 3: 'C#', 4: 'SQL'}
a = slovnyk[1]
print(a)

mova = int(input('Введіть свою мову'))

if mova in slovnyk:
    print('Mova', slovnyk[mova])
else:
    print('Error')

try:
    print('Mova', slovnyk[mova])
except KeyError:
    print('NOT')

mova = int(input('Введіть свою мову'))
print(slovnyk.get(mova))'''

'''slovnyk1 = {'Prog1': 'Python', 'Prog2': 'C++'}
slovnyk2 = {'work': slovnyk1}
slovnyk3 = {'work': {'Prog1': 'Python', 'Prog2': 'C++'}}
print(slovnyk1)
print(slovnyk2)
print(slovnyk3)'''

'''slovnyk1 = {'Prog1': 'Python', 'Prog2': 'C++'}
print(len(slovnyk1))

posit = {'Admin': {'Admin1', 'Admin2', 'Admin3'}, 'Prog': {'Python', 'SQL'}}
print(len(posit))
print(len(posit['Admin']))'''

'''days = {1: 'Py', 2: 'C++'}
print(days[1])
days[2] = 'C#'
days[3] = 'SQL'
print(days)
del days[3]
print(days)'''

'''words = dict()
count = int(input('Кількість слів'))
i = 0
while i < count:
    klych = input('Введіть ключ')
    znachennya = input('Введіть переклад')

    if klych not in words:
        words[klych] = znachennya
    i += 1
print(words)'''

'''diction = {1: '1', 2: "2"}
print(diction)
diction.clear()  # видалення елементів в середині словника
print(diction)

diction1 = {1: 'A', 2: "B"}
d2 = diction.copy()
print(diction1)
print(d2)

diction1['C'] = 3
d2['A'] = 'one'
print(diction1)
print(d2)

d3 = dict.fromkeys([1, 2, 3])  # створити новий словник з ключів
print(d3)
d4 = dict.fromkeys([1, 3, ], 'A')
print(d4)

d5 = dict.fromkeys([1, 2], ['A', 'B'])
print(d5)

d6 = {'1': 'o', '2': 'b'}
n = d6.items()
print(n)
n2 = dict.items(d6)
print(n2)

d7 = {'a': 1, 2: 'b'}
n3 = d7.keys()
print(n3)
n4 = iter(d7)
print(list(d7))
n5 = d7.values()
print(list(d7))  # список ключів

n6 = d7.values()
print(n6)
print(list(n6))  # Список значень

d8 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
item = d8.pop(2)  # видаляємо елемент зі словника і витягужмо записуємо змінну його значення
print(item)
print(d8)

d9 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
item = d9.popitem()
d10 = {1: 'A', '2': 'VV'}
item2 = d10.popitem()  # видаляє останню пару і записує її змінну
print(item)
print(item2)
print(d9)
print(d10)

d11 = {'R': 1, 'B': 2, 'G': 3}
item = d11.setdefault('G')
print(item)
print(d11)

item2 = d11.setdefault('W')
print(item2)
print(d11)

item3 = d11.setdefault('H', 8)
print(item3)
print(d11)

d12 = {'R': 1, 'B': 2, 'G': 3}
d12.update([('F', 3), ('E', 4)])
print(d12)'''
# 111
# 222
# 333

'''users = [{'name': 'Anna', 'age': 10, 'login': 'user56'},
         {'name': 'Ivan', 'age': 33, 'login': 'user23'},
         {'name': 'Jack', 'age': 30, 'login': 'user54'},
         {'name': 'Alice', 'age': 25, 'login': 'user15'},
         {'name': 'Alice', 'age': 25, 'login': 'user13'}]
print(users)

keyName = input('інфо тип')
keyValue = input('інфо велю')
if keyName == 'age' and keyValue.isdigit() == True:
    keyValue = int(keyValue)
isElementFound = False
for user in users:
    if user.get(keyName) == keyValue:
        print('Element is found')

        for key, val in user.items():
            print('{}:{}'.format(key, val))
        isElementFound = True
        # break
if isElementFound == False:
    print('Element is not found')'''

# 111
# 222
# 333


'''my_dict = {
    'Nick': {'Phone': '0934646138', 'telega': {'official': '@nick_11', 'privat': '@nicprivat'}, 'insts': '@nice555'},
    'Ann': {'Phone': '0999299201', 'telega': '@ann_11', 'insts': '@ann588'},
    'Ivan': {'Phone': '090800800', 'telega': '@ivan_1', 'insts': '@nice555'}}
name = input('Введіть імя').title()
contact_type = input('введіть тип даних').lower()
user = 0
try:
    if contact_type == 'telega':
    type_tg = input('privat or off').lower()
    user = my_dict[name][contact_type][type_tg]
    print(user)
    else:
        user = my_dict[name][contact_type]
    print(user)
except:
    print('d')
'''
# user = my_dict[input('Введіть імя').title()][input('введіть тип').lower()]
# print(user)

##
dictionary = {"привіт": "hello", "дякую": "thank you", "до побачення": "goodbye"}


def translate_word(word):
    if word in dictionary:
        return dictionary[word]
    else:
        answer = input(f"Слово '{word}' не знайдено. Бажаєте додати його до словника? (так/ні) ")
        if answer == "так":
            translation = input(f"Який переклад слова '{word}'? ")
            dictionary[word] = translation
            return f"Слово '{word}' успішно додано до словника з перекладом '{translation}'"
        else:
            return f"Переклад слова '{word}' не знайдено"


def print_dictionary():
    print("Словник:")
    for word in dictionary:
        print(f"{word} - {dictionary[word]}")


while True:
    print("\nМеню:")
    print("1. Перекласти слово")
    print("2. Показати словник")
    print("3. Вийти з програми")
    choice = input("Ваш вибір: ")

    if choice == "1":
        word = input("Яке слово потрібно перекласти? ")
        translation = translate_word(word)
        print(translation)
    elif choice == "2":
        print_dictionary()
    elif choice == "3":
        print("До побачення!")
        break
    else:
        print("Неправильний вибір. Спробуйте ще раз.")
