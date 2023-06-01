# spysok = [2, 4, 7, 12, 11, 23, 56, 89, 78, 1, 59]

'''b = 0
for i in spysok:
    b += i

print(b)
'''
'''

def calcSum(A):
    if A == []:
        return 0
    else:
        summ = calcSum(A[1:])
        summ += A[0]
        return summ


summ = calcSum(spysok)
print(summ)
'''
'''
spysok = [-2, 4, -7, -12, 11, -23, 56, -89, 78, 1, 59]


def calcSumNeg(A):
    if A == []:
        return 0
    else:
        count = calcSumNeg(A[1:])
        if A[0] < 0:
            count += 1

        return count


n = calcSumNeg(spysok)
print(n)
'''

'''
def GetFiblist(n, L):
    count = len(L)
    if len(L) < 2:
        return []

    num1 = L[count - 2]
    num2 = L[count - 1]

    if (num1 + num2) < n:
        L = L + [num1 + num2]
        return GetFiblist(n, L)
    else:
        return L


new = GetFiblist(100, [0, 1])
print(new)'''

'''
def Power(x, y):
    if y > 0:
        return x * Power(x, y - 1)
    else:
        return 1


x = 3
y = 4
res = Power(x, y)
print(res)'''

##
'''
def GetMaxList(L):
    if len(L) > 1:
        Max = GetMaxList(L[1:])
        if L[0] < Max:
            return Max
        else:
            return L[0]

    if len(L) == 1:
        return L[0]


spysok = [500, 6000, 40, 53]
res = GetMaxList(spysok)
print(res)
'''
#
'''#
while True:

    user_list = input("Введіть елементи списку, розділені пробілами: ").split()
    user_list = [int(num) for num in user_list]
    operation = input("Виберіть операцію: \n1 - Пошук найменшого елементу,\n"
                      "2 - Кількість позитивних чисел: ")


    def find_cheapest_element(lst):
        if len(lst) == 1:
            return lst[0]
        else:
            rest_cheapest = find_cheapest_element(lst[1:])
            return lst[0] if lst[0] < rest_cheapest else rest_cheapest


    def count_positive_numbers(lst):
        if len(lst) == 0:
            return 0
        else:
            rest_count = count_positive_numbers(lst[1:])
            if lst[0] > 0:
                return 1 + rest_count
            else:
                return rest_count


    if operation == "1":
        result = find_cheapest_element(user_list)
        print("Найменший елемент у списку:", result)
    elif operation == "2":
        result = count_positive_numbers(user_list)
        print("Кількість позитивних чисел у списку:", result)
    else:
        print("Невірний вибір операції.")

'''

#
'''def simpleD(myFun):
    print('Helo!')

    def simpleW():
        print('Func starts...')
        myFun()
        print('See you!')

    return simpleW()

def simpleD_2(myFun)
    print('hhello')
    def

# @simpleD
def sayHi():
    print('Welcome')


# sayHi()

def sayBye():
    print('Bye')


sayBye = simpleD(sayBye)
sayBye()

'''

# new_ver = simpleD(sayHi)
# new_ver()
'''
def simpleDecoration_v3(myFunction):
    print('I m 3rd')

    def simpleWrapper():
        print('Func start')
        result'''

#
