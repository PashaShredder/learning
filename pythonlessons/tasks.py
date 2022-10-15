# number = 3453773459
# result = 0
# while number != 0:
#     result += number % 10
#     number //=10
# print(result)
#
# res = list(str(number))
# result = 0
# for i in res:
#     result += int(i)
# print(result)
#
# l = [1,3,7,7,43,6]
#
# def find_num(w):
#     counter = 0
#     index = 0
#     for i in w:
#         if i ==7:
#             counter += 1
#             if counter == 7:
#                 return index
#         index +=  1
#
# print(find_num(l))
#
# a = [1,4,56,6,7,77,'4','a',55]
# low5 = []
# for i in a:
#     if type(i) == str:
#         if i.isdigit():
#             i = int(i)
#             if i < 5:
#                 low5.append(i)
#     else:
#         low5.append(i)
#
# print(low5)

"""общие элементы списка из 2х"""
# c = [1,1,2,3,7,6,7,8,4,8,99]
# b = [1,7,7,7,99,99,8,3,6,4,4,11]
#
# list= []
# for i in c:
#     if i in b:
#         list.append(i)
# print(list)

"""слияние словарей в один"""

# dict_a = {1: 10, 2: 20}
# dict_b = {3: 30, 4: 40}
# dict_c = {5: 50, 6: 60}
#
#
# a = {}
# a.update(dict_a)
# a.update(dict_b)
# a.update(dict_c)
# print(a,b,c)
#
#
# list = [dict_a,dict_b,dict_c]
# def un_dict(list):
#     a ={}
#     for i in list:
#         a.update(i)
#     return a
#
# print(un_dict(list))

""" 2 списка -- выводит все элементы 1го, 
которых нет во 2м"""

# set_1 = set(['White','Black','Red','Green'])
# set_2 = set(['Black','Red'])

# print(set_1.symmetric_difference(set_2)) # убирает дубли
# print(set_1.difference(set_2))
# print(set_1 - set_2)

"""проверка на уникальность последовательности"""

# u = [1,2,3,4,5,4,3,2,4,5,6,7]
# b = set(u)
# if u == list(b):
#     print('без дублей')
# else:
#     print('есть дубли')

""" сортировка словаря по значениям или ключам"""
# a = {
#     1: 25,
#     2: 55,
#     3: 77
# }
# b ={
#     4: 12,
#     5: 21,
#     6: 99
# }
# c ={
#     7: 1,
#     8: 49,
#     9: 72
# }
#
# lst = [a,b,c]
# D = {}
#
# for i in lst:
#     D.update(i)
#
# # result_dict = sorted(D.values())# по значениям
# result_dict = sorted(D,key=D.get)
#
# print(D)
# print(result_dict)
# new_D={}   # по ключам
# for key in result_dict:
#     new_D[key] = D[key]
#
# print(new_D)

"""определить самую длинную и короткую строку
/ удалить пустые строки"""

# stroka = "String will never be empty and you do          not need to a account for different data types."
# slova = stroka.split()
# print(slova)
# long_min = 999
# long_max = 0
# for i in slova:
#     if len(i) < long_min:
#         long_min = len(i)
#         short = i
#     if len(i) > long_max:
#         long_max = len(i)
#         long = i
# print(short)
# print(long)

'''найти наичаще встречающиеся слова /
 сколько раз каждое слово встречается в строке'''

# stroka = "String will never be empty and you do do do do a a a  a       a a a not need to a account for different data types."
# slova = stroka.split()
# kolvo =0
# dict = {}
# for i in slova:
#     kolvo = slova.count(i)
#     dict[i] = kolvo
# print(dict)

"""на примере Банк карты спрятать всё
 кроме последних 4-х символов"""

# string = '5465 7788 2131 6577'
# new = ''
# for i in range(len(string) - 4):
#     if string[i] != ' ':
#         new += '*'
#     else:
#         new += ' '
# new += string[-4:]
# print(new)

""" добавление чисел(чётных) в список кратных 
двум(делёными на 2 без остатка)"""
#
# numbers = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         numbers.append(i)
#
"""(генераторы списков) запись чисел внутрь списка"""
# numbers = [i for i in range(1,11)]
# numbers = [i for i in range(1,11) if i % 2==0] #кратным 2м
# print(numbers)
"""создание матрицы"""

# from  random import randint
# n = 3
# matrix = [[randint(1,9) for j in range(n)]for i in range(n)]
# print(matrix)

""" посчитать ко-во символов в ключе и 
добавить в конце ключа число символов /
 генератор словаря """
#
# a = {"wertrtyry": "2",
#      "rwtf": "55",
#      "ratrtyy": "17"
#      }
#
# a2 = {}
# for i in a:
#     a2[i + str(len(i))] = a[i]  # добавляем в новый словарь ключи+ к-во символов к ним
#
# print(a2)
#
# a3 = {i + str(len(i)): a[i] for i in a}
# print(a3)
# # {key: value for item in list if conditional} конструкция генераторы словаря

"""(задача с реального проекта)таблица ключи - название колонки,
 значение - тип данных колонки(список колонок--вернуть словарь 
 который содержит конкретные колонки и тип данных которые они хранят
 3 ключа - 3 значения ключей"""

# D = {"integer":'int',"string":'str',"tuple":'tpl',"set":'set', "dicttionary":'dict',"list":'list',"Boolean":'bool'}
# lst = ["integer", "string", "list"]
# Dict_new = {i:D[i] for i in D if i in lst}
# print(Dict_new)

"""ГЕНЕРАТОРЫ (yield- аналог return для генераторов)
(next - обращение к следующему элементу) 
возвращает значение но не хранит его/ удобны 
когда известно что ф-ция вернёт большой набор значений, которые надо прочитать только 1 раз"""

# mygenerator = (x*x for x in range(3)) # конструцкия

# def create_generator():
#     mylist = range(3)
#     for i in mylist:
#         yield i*i

"""создание скриптов
библиотека argparse-для упращения работы со скриптами"""
#
# import sys, argparse
#
# print(sys.argv)
#
# if "Pavel" in sys.argv:
#     print("Hi, Pavel")
# else:
#     print("Who are you?")
#
# print(sys.argv)
# parser = argparse.ArgumentParser()
# parser.add_argument("-fn", "--first-name", required=True)
# parser.add_argument("-ln", "--last-name", required=True)
# parser.add_argument("echo")
# args = parser.parse_args()
# print(args)
# print("First name:", args.first_name)
# print("Last name:", args.last_name)
# print("echo", args.echo)

"""найти сумму с помощью генераторов"""

#
# def num(x):
#     lists = list(str(x))
#     d = [int(i) for i in lists]
#     return sum(d)
#
#
# n = 28340928374
# print(num(n))
"""поиск числа по индексу"""


# def ind_3(a):
#     return [i for i in range(len(a)) if a[i] == 3][2]
#
#
# print(list(enumerate([1, 2, 3, 3, 3, 3])))
# print(ind_3([1, 2, 3, 3, 3, 3]))

