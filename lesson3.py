# print('Hello!')
#
# print('Hello!', end='-->')
# print('Hello!')
#
# print('Hello!', 'World')
# print('Hello!', 'World', 'hi')
# print('Hello!', 'World', 'hi', sep='-->')
#
# print('''
# 1
# 1
# 1
# 12
# 2
# ''')
#
# number_1 = input('number_1 = ')
# print(type(number_1))
#
# number_1 = 25
# number_2 = 2
# # print(number_1 / number_2)
# try:
#     number_3
#     print(number_1 / number_2)
# except:
#     print('error')

# try:
#     x = 5
#     y = '3'
#     print(x ** y)
# except:
#     print('Error')
#
# error = 33
# try:
#     print('start code')
#     print(error)
#     print('no errors')
# except:
#     print('We have an error')
# print('\n\t\tcode after capsule')

'''
try:
    print('start code')
    # print(error)
    print(15/0)
    print(error)
    print('no errors')
# except NameError:
#     print('We have NameError error')
# except ZeroDivisionError:
#     print('We have an ZeroDivisionError')
except (NameError, ZeroDivisionError) as error:
    print(error)

print('\n\t\tcode after capsule')'''

'''try:
    try:
        print('start core')
        print(10/0)
        print(error_1)
        print('no errors')
    except NameError as error:
        print(error)
except ZeroDivisionError as error:
        print(error)'''

# try:
#     print('Hello')
# except:
#     print('! problems')
# else:
#     print('no problems')
# finally:
#     print('Finally code')
'''!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import  tkinter as tk
# 
# root = tk.Tk()
# root.title('first')'''

# try:
#     apples = int(input('Введіть кількість яблук: '))
#     if apples < 0:
#         raise Exception
#     print('Ти маєш', apples, 'яблук.')
# except Exception:
#     print('Ти не можеш мати', apples, 'яблук.')
# finally:
#     print('ok')

# try:
#     apples = int(input("Enter the amount of apples: "))
#     if apples < 0:
#         raise Exception
#     print("you have", apples, "apples")
# except Exception:
#     print("You make mistake")
# finally:
#     print("OK")
#
# try:
#     try:
#         apples = int(input("Enter the amount of apples: "))
#         if apples < 0:
#             raise Exception
#         print("you have", apples, "apples")
#     except Exception:
#         print("You make mistake", apples)
# except:
#     print('Error')

# try:
#     raise ValueError
# except ValueError:
#     print('Improper value was obtained')
# except Exception:
#     print('.... Somethin went wrong')
#
# try:
#     f = open('some_text.txt')
# except ZeroDivisionError:
#     print('Error 1')
# except:
#     print('Errors...')

# day = 4
# month = 'april'
# year = 2023
#f
# print('Today is', day, month, year, '.')
# print(f'Today is {day} {month} {year}.')
# print(f'Today is {day:8} {month:15} {year:10}.')
# print(f'Today is {day:^8} {month:<15} {year:>10}.')
# print(f'Today is {day:_^8} {month:*^15} {year:%^10}.')

# #format
# print('Today is {} {} {}.'.format(year, month, day))
# print('Today is {:%^10} {:*^15} {:_^}.'.format(year, month, day))
# print('Today is {:_^10.3f} {:*^15} {:_^}.'.format(year, month, day))
# print('Today is {year:_^10.3f} {month:*^15} {day:_^}.'.format(year=2022, month='aprile', day=22))





