"""вывод имён из списка через цикл"""

# def hello_name(name):
#     return f"Hello, {name}"
#
#
# list = ['Alex', 'Bob', 'Robert', 'Olga', 'Pavel']
# for i in list:
#     print(hello_name(i))

"""сложение элементов из функции при
помощи цикла"""

# def summ_data(*args, **kwargs):
#     summ = 0
#     for i in args:
#         summ = summ + i
#     return summ
#
#
# summ = summ_data(7, 7, 8, 5, 9)
# print(summ)

"""конкатенация(сложение)
 строк и чисел циклом"""
# def summ(*args):
#     result = 0
#     result_str = ""
#     t = True
#     for i in args:
#         if str(i).isdigit():
#             t = False
#     if t == True:
#         for i in args:
#             result += i
#         return result
#     else:
#         for i in args:
#             result_str += str(i)
#         return result_str
#
#
# print(summ("qqwert", 4, 6, 7, 23, "tuptup"))
"""вывести лесенку """
# def stairs(*args):
#     return  args
#
# r = ''
# for i in range(0,9):
#     r += str(i)
#     print(*stairs(r))

"""удаление дубликатов из списка + 
сами повторяющиеся значения"""

# def my_list(lst):
#     list_2 = []
#     for i in lst:
#         if lst.count(i) < 2: # считает только те элементы, которые встречаются меньше 2 раз
#             list_2.append(i)
#     return list_2
#
#
# list = [1, 2, 3, 4, 4, 3, 7, 7, 9, 9]
# print(my_list(list))
"""удаление дубликатов """
# def list_delete(list):
#     list_2= []
#     for i in list:
#         if i not in list_2:
#             list_2.append(i)
#     return list_2
# list = [1, 2, 3, 4, 4, 3, 7, 7, 9, 9]
# print(list_delete(list))


""" нахождение числа без противоположного 
знака(пара чисел)"""

# def func(list):
#     list_2 = []
#     for elem in list:
#         if -elem not in list:
#             list_2.append(elem)
#
#     return list_2
#
#
# list = [1, -1, 2, -2, 4, -4, 3]
# print(func(list))
