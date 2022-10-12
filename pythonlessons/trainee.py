""" проверка на введённые данные если да(результат)
если нет(ничего)"""
# name = input('Enter your name \n')
# age = int(input('Enter your age \n'))
# if age >= 18 and age < 60:
#     print(f"{name}, you are adult")
# else:
#     print(f"{name}, you are underage")
""""проверка на палиндром (одинаково читаемое 
слово слева на право и наоборот) """
# string = input()
# if string == string[::-1]:
#     print("yep")
# else:
#     print("no")
"""цикл для работы со вложенными списками(матрица)"""
# for i in [[1,2,3],[4,5,6],[7,8,9]]:
#     for j in i:
#         print(j)
"""нумерация каждый елемент 
списка(возможность работать с индексами)"""
# for i, elem in enumerate(['a','b','c','d']):
#     print(f'{i}-{elem}')
"""удаление дубликатов циклом"""
# list = [2, 3, 5, 5, 5, 6, 2, 25, 68, 8, 9, 56, 6, 7, 7, 77, 7]
# list2 = []
# for i in list:
#     if i in list2:
#         continue
#     else:
#         list2.append(i)
#     print(list2)
""""вывести значение больше/меньше чем(...) циклом """
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in list:
#     if i < 5:
#         print(i)
#     elif i >5 and i <8:
#         print(i**2)
#     else:
#         print(i**3)
""" """