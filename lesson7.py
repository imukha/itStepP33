'''userTypes = ['admin', 'student', 'teacher']
userTypes[0] = 'user'

a = (1, 2, 3, [1, 2])
a[3][1] = 4
print(a)
'''

'''myTuple = ()
myTuple1 = tuple()
print(myTuple)
print(type(myTuple))
print(myTuple1)
print(type(myTuple1))'''

'''myTuple1 = ('element1', 12, 35.6, False)
myTuple2 = ('item1',)
myTuple3 = ('admin', 'student', 'teacher')
myTuple4 = 'Name',

print('myTuple1:', myTuple1, 'type: ', type(myTuple1))
print('myTuple1:', myTuple2, 'type: ', type(myTuple2))
print('myTuple1:', myTuple3, 'type: ', type(myTuple3))
print('myTuple1:', myTuple4, 'type: ', type(myTuple4))'''

'''itemTuple = (1, 2, 1, 2)
print(itemTuple)'''

'''nameTuple1 = tuple(('Hi', 'Buy'))
nameTuple2 = tuple(('Hi', 'Buy'))
print(nameTuple1)
print(nameTuple2)'''

'''users = ('admin', 'student', 'hr', 'moderator')
print('1st user', users[0])
print('last user', users[len(users) - 1])
print('...:', users[-1])
print('...:', users[:2])
print('...:', users[1:3])
# users[0] = 'user'
del users
print(users)'''

'''danni = ('Mon', 'Tue', 'Wes', 'Thu')
day1, day2, day3, day4, = danni
print(day1)
print(day2)
print(day3)
print(day4)

danni1 = ('Python', 'Java', 'C++', 'C#')
mova, *movi = danni1
print(mova)
print(movi)'''

'''cifri = (1, 2, 3, 4)
num, *nums, num2 = cifri
print(num)
print(nums)
print(num2)'''

'''cort = (True, False, 'Some inf', 4)

for danni in cort:
    print(danni)

for i in range(len(cort)):
    print(cort[i])'''

'''a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)

d = (3, 'sst') + (-25.2, ['ssddd', False])
print(d)

n = ('str', 'stroka')
s = n + (5, 6)
print(s)'''

'''cort = (1, 2, 1, 3) * 3
print(cort)

cort1 = ('ss', 'sssd')
for i in cort1 * 5:
    print(i)
    '''

'''myTuple = ('admin', 'student', 'teacher', 'admin')
print(myTuple.count('admin'))
'''

'''while True:
    firstName = input('Input your first name')
    lastName = input('Input your last name')
    yearBirth = input('Input your Birth year')
    gender = input('Input your (M, F)')
    if firstName == '' or lastName == '' or yearBirth == '' or gender not in ('F', 'M'):
        print('Wrong data')

    else:
        info = (firstName, lastName, yearBirth, gender)
        print(info)

    hobbyInd = 1
    hobbyList = []
    while True:
        hobbyName = input('Name of the hobby #{}:'.format(hobbyInd))
        if hobbyName == '':
            print('No info')
            break
        else:
            hobbyList.append(hobbyName)
            hobbyInd += 1

    if len(hobbyList) > 0:
        print(f'You have{hobbyInd - 1} hobbies')
    else:
        print('You dont have hobbi')

    progId = 1
    infoprog = []
    while True:
        prog = input(f'Name of prog lang {progId}')
        if prog == '':
            print('u didnt')
            break
        else:
            infoprog.append(prog)
            progId += 1
    if len(infoprog) > 0:
        print(f'You know {progId - 1} prog lang')
    else:
        print('You dont know pro')'''

'''fruits = ('banana', 'apple', 'bananamango', 'mango', 'strawberry-banana', 'banana')
fruit_name = input('Введіть назву фрукта: ')

fruit_count = 0
for fruit in fruits:
    if fruit_name in fruit:
        fruit_count += 1
print('Кількість фруктів "{}" в кортежі: {}'.format(fruit_name, fruit_count))
'''

# УРОК №2

'''mySet1 = {1, 2, 3}
mySet2 = {'bob', 'joe', 'kate'}
mySet3 = {'bob', 23, False, (33.3, 44)}
print(mySet1)
print(mySet2)
print(mySet3)

mySet4 = set((10, 20, 30))
print(mySet4)'''

'''a = {'Joe', 'Joe', 'Bob', 'Kate'}
print(a)
spysok = ['Joe', 'Joe', 'Bob', 'Kate']
new_m = set(spysok)
print(new_m)
print(list(new_m))
'''

'''A = {1, 2, 3, 4}
B = {4, 3, 2, 1}
print(A == B)
'''
'''
userName = {'Joe', 'Joe', 'Bob', 'Kate'}
for name in userName:
    print(name)'''
'''
userName = {'Joe', 'Joe', 'Bob', 'Kate'}
name = input('You name')
if name in userName:
    print('Welcome', name)'''

'''mySet = {1, 2, 3}
print(mySet)
mySet.add(4)
print(mySet)
mySet.update([3, 4, 5])
print(mySet)
mySet.update([5, 5], {12, 2, 12, 15})
print(mySet)
mySet.discard(12)
print(mySet)
mySet.discard(10)
print(mySet)
'''  # & \ -

'''studGroup1 = {'Joe', 'Bob', 'Kate'}
studGroup2 = {'Ivan', 'Joe', 'Bob', 'Sem'}
print('Перетин')
print(studGroup1 & studGroup2)
print(studGroup1.intersection(studGroup2))

print('Обєднання')
print(studGroup1 | studGroup2)
print(studGroup1.union(studGroup2))

print('Різниця')
print(studGroup2 - studGroup1)
print(studGroup2.difference(studGroup1))'''

# allPizzaTupes = []
# while True:
#     a = input('d you w p')
#     if a == 'y':
#         b = input('pizza')
#         allPizzaTupes.append(b)
#     else:
#         print('not')
# pizza_un = list(set(allPizzaTupes))
# print(pizza_un)


'''userApp1 = ['user134', 'admin56', 'superBob', 'student', 'spider34']
userApp2 = ['fifa22', 'user134', 'StudGood']

print('користувачі двох')
print(set(userApp1) & set(userApp2))

print("кор тільки першого")
print(set(userApp1) - set(userApp2))

print("кор т 2")
print(set(userApp2) - set(userApp1))

print("усі кор")
print(set(userApp1) | set(userApp2))

word1 = input('fors word')
word2 = input('2 word')

if set(word1) == set(word2):
    print('Yes')
else:
    print('no')

sp = []
import random

i = 0
while i < 10:
    d = (random.randrange(0, 5))
    sp.append(d)
    i += 1

print(sp)
cort = tuple(sp)
print(cort)
'''

t1 = (1, 2, 3, 5)
t2 = (2, 2, 4, 5)
t3 = (3, 2, 5, 5)

common_elements = []
for i in range(min(len(t1), len(t2), len(t3))):
    if t1[i] == t2[i] == t3[i]:
        common_elements.append(t1[i])

print(common_elements)
