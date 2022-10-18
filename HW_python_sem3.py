# Задача 1 Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list = [2, 3, 5, 9, 3]
print(sum(list[1::2]))

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 5, 6]

list_mult = []

for i in list:
    list_mult.append(list[0] * list[-1])
    list.pop(0)
    list.pop()

print(list_mult)

list = [2, 3, 4, 5, 6]

list_mult = []

if len(list) % 2 != 0:
    for i in range(len(list)//2 + 1):
        list_mult.append(list[i] * list[len(list)-i-1])

print(list_mult)

# Задача 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from decimal import Decimal

list = [1.1, 1.2, 3.1, 5, 10.01]
list_fractional_part = []

for i in list:
    list_fractional_part.append(Decimal(i - int(i)))

print(list_fractional_part)

result = max(list_fractional_part) - min(list_fractional_part)
result_str = str(result)
# print(type(result_str))

print((result_str[:result_str.find('.')+3]))

# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Нельзя использовать готовые функции.
#
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Введите целое число: "))

bin_number = ''

while number > 0:
    bin_number = str(number % 2) + bin_number
    number = number // 2
    print(bin_number)

print(bin_number)
