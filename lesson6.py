'''a = '-----test. It! step Text-----'
print(a.strip())
print(a.center(90))
print(a.strip('-'))

a = [12, 15, 20, 30, 50, 40, 100, 200, 55]
student = ['Alex', 'Ivan', 'Jul', 'AS', 'Oleg', 'Dj']

print(student)
print('Hi!', student[0])
print(student[1:3])
print(student[3])
# print('Hi!', student[1])
# print('Hi!', student[2])
# print('Hi!', student[3])
# print('Hi!', student[4])
print('Hi!', student[3])

# додавання елементу app
a = [12, 15, 20, 30, 50, 40, 100, 200, 55]'''

'''print(a)
a.insert(2, 99)
print(a)

a.append(12)
print(a)
a.extend([1, 2, 5, 4])
print(a)

# видалення revove
a = [12, 15, 20, 30, 50, 40, 100, 200, 55]
student = ['Alex', 'Ivan', 'Jul', 'AS', 'Oleg', 'Dj']

print(student)
del (student[1])

print(student)
i = student.index('AS')
print(i, student[i])

del (student[i])
print(student)

# зміна редагування edit

student = ['Alex', 'Ivan', 'Jul', 'AS', 'Oleg', 'Dj']
print(student)
student[1] = 'IVANNN'
print(student[5])

## CREAT
# 1) creat
# 2) read
# 3) append item
# 4) remove
# 5) edit

student = ['Alex', 'Ivan', 'Jul', 'AS', 'Oleg', 'Dj']
for item in student:
    print('Hi!', item)
    print(item, [10, 11, 10, 12])

for i in range(len(student)):
    print(i, student[i])
for i in range(len(student)):
    print()
'''
'''# Практична
# 1
student = ['Alex', 'Ivan', 'Jul', 'AS', 'Oleg', 'Dj']
a = [12, 15, 20, 30, 50, 40, 100, 200, 55]
print()
# 2
print(student[0])

# 3
a[-1] = 999
for item in a:
    print(item)

# 4
st_a = student + a
print(st_a)
'''

# lesson6_2
'''
list_1 = [
    [12, 15],
    [20, 30, 50, 40],
    [100, 200, 55]
]
print(list_1)
for item in list_1:
    print(item)
print(list_1[0])
print(list_1[0][1])

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b + a
print(c)

a = [1, 2, 3] * 5
print(a)

a = [[12, 12, 12]] + [[0, 0, 0, 0]] * 100
print(a)

mylist = ['a', 'b', 'c', 'd', 'e']
print(mylist)
mylist[0:3] = [0, 0, 0, 0]
print(mylist)

mylist = [12, 15, 20, 30, 50, 40, 100, 200, 55]
mylist.append(6)
print(mylist)

L = [7, 8, 9, 10]
mylist.extend(L)
print(mylist)

mylist.insert(1, 1000)
print(mylist)

mylist = [12, 15, 4, 4, 20, 30, 50, 40, 100, 200, 55]
mylist.remove(4)
mylist.remove(4)
print(mylist)

val = mylist.pop(2)
print(mylist)
print(val)
'''
'''
mylist = [12, 15, 4, 4, 20, 30, 50, 40, 100, 200, 55]
i = mylist.index(20)
print(i)
print(mylist.count(4))
print(4 in mylist)
'''
'''
mylist = [12, 15, 4, 4, 20, 30, 50, 40, 100, 200, 55]
print(mylist)

mylist.sort()
print(mylist)

mylist.sort(reverse=True)
print(mylist)

print(mylist[0])

student = ['Alex', 'Ivan', 'Jul', 'AS', 'Oleg', 'Dj']
print(student)

student.sort()
print(student)

student.sort(reverse=True)
print(student)

mylist.reverse()
print(mylist)

mylist.clear()
print(mylist)
'''
'''
student = ['Alex', 'Ivan', 'Jul', 'AS', 'Oleg', 'Dj']
print(len(student))

a = [12, 15, 4, 4, 20, 30, 50, 40, 100, 200, 55]
print(max(a))
print(min(a))
print(sum(a))
print(int(sum(a) / len(a)))
b = sorted(a)
c = sorted(a, reverse=True)
print(a)
print(b)
print(c)

a = [12, 15, 4, 4, 20, 30, 50, 40, 100, 200, 55]
b = a.copy(a)
a[0] = 11
print(a)
print(b)

a = [12, 15, 4, 4, 20, 30, 50, 40, 100, 200, 55]
b = a.copy()
print(a)
print(b)
'''

import random

nums = []
for i in range(100):
    nums.append(random.randint(-100, 100))
print(nums)
'''
import random

nums = []
for i in range(100):
nums.append(random.randint(-100, 100))

print(nums)'''
