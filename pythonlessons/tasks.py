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

