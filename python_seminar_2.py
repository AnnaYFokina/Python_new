# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

number = list(input("Введите вещественное или целое число: "))
print(number)

summ = 0
for i in number:
    if i != "," and 1 != '.' and 1 != '-':
        i = int(i)
        summ = summ + i

print(summ)

# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

size = int(input("Введите число N: "))

number_multiple_list = []
start_number = 1
for i in range(size):
    print(i)
    start_number = start_number + start_number * (i)
    number_multiple_list.append(start_number)

print(number_multiple_list)

# Задача 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой. Нельзя юзать find или count.

str_1 = input('Введите первую строку: ')
str_2 = input('Введите вторую строку: ')

str_new = str_1.split(str_2)
print(str_new)
print(len(str_new))
print(f'Число вхождений второй строки в первую - {len(str_new)-1}')

# compare_result = (str_2 in str_1)
# print(compare_result)
#
# if compare_result == True:
#     str_replaced = str_1.replace(str_2, '1')
#     print(str_replaced)
# else:
#     print("В первой строке нет вхождений второй строки")
#
# str_replaced = list(str_1)
# print(str_replaced)

# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, и координаты двух точек
# и находит расстояние между ними в N-мерном пространстве.

import math
#AB = √(xb - xa)2 + (yb - ya)2 + (zb - za)2 - формула вычисления расстояния между точками в n-мерном простанстве

n = int(input('Введите размерность пространства: '))
sq = 0
sq_all = 0
for _ in range(1, n*2+1):
    i = int(input(f"Введите {i} координату точки: "))
    sq = ((i-1)-i) ** 2
    sq_all = sq_all + sq

print(math.sqrt(sq_all))

