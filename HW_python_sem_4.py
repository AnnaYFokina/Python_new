# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i += 1
   if n > 1:
       primfac.append(n)
   return primfac
print(primfacs(21))

# задача 2 . Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint

my_list = [randint(1, 10) for i in range(1, 20)]
print(my_list)
new_set = set(my_list)
print(new_set)
print(list(new_set))


# задача 3. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = 10
k_result = ''
k_count = 10
for i in range(0, k):
    koef = str(randint(0, 100))
    k_count_str = str(k_count)
    k_result = k_result + koef + "x**" + k_count_str + "+"
    k_count -= 1
koef_last = str(randint(0, 100))
k_result = k_result + koef_last + ' = 0'
print(k_result)

with open ('file.txt', 'w') as data:
	data.write(k_result)


# задача 4 необязательная. Найдите корни квадратного уравнения,
# уравнение вводит через строку пользователь. например, 6*x^2+5*x+6=0 .
# Само собой, уравнение может и не иметь решения. Предусмотреть все варианты, сделать обработку исключений.
# 12*x2+12b+12 = 0

strin = input("Введите уравнение вида A*x²+B*x+C = 0, возведение в квадрат обозначьте как '2' после x: ")
a = '1'
a_count = 2
for i in range(len(strin)-1):
    if strin[i]=='x':
        if strin[i+1] == '2' and strin[i-(a_count)].isdigit():
            a = a + (strin[i-(a_count)])
            a_count += 1

b = '1'
b_count = 1
for i in range(len(strin)-1):
    if strin[i]=='x':
        if strin[i+1] != '2' and strin[i-(b_count)].isdigit():
            b = b + (strin[i-(b_count)])
            b_count += 1

a = int(a)
b = int(b)
print(a, b)
new_strin = strin.split('x')

last_coef_element = new_strin[-1]
print(last_coef_element)

c = ''

for i in range(0, len(last_coef_element)):
    if last_coef_element[i].isdigit() and last_coef_element[i] != "0":
        c = c + last_coef_element[i]

print(c)
c = int(c)

# 12A*x2+8*x+12 = 0
d = b * b - 4 * a * c
x_1 = (-b) + d ** 0,5 / 2 * a
x_2 = (-b) - d ** 0,5 / 2 * a
print(d)
if d < 0:
    print("Нет корней в области вещественных чисел")
elif d > 0:
    print(f'Уравнение имеет два корня {x_1} и {x_2}')
else:
    print(f'Оба корня равны {x_1}')