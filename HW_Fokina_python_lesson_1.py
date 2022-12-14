# задача 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
#
# *Пример:*
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет


a = int(input("Введите число от 1 до 7: "))
if a in range(1,6):
    print("да")
elif a == 6 or a == 7:
    print("нет")
else:
    print("Введите корректные данные")

# задача 2. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            if (not (x or y or z)) == True and (not x and not y and not z) == True:
                print(f"Утверждение истинно")
            else:
                print(f"Утверждение ложно")

# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x_abs = int(input("Введите координату точки во оси Х: "))
x_ord = int(input("Введите координату точки во оси Y: "))

if x_abs > 0 and x_ord > 0:
    print("1")
elif x_abs > 0 and x_ord < 0:
    print("4")
elif x_abs < 0 and x_ord > 0:
    print("2")
else:
    print("3")

# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число,
# второе число и операцию, после чего применяет операцию к введённым числам
# ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где mod — это взятие остатка от деления,
#  pow — возведение в степень, div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.

x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
z = str(input('Введите знак операции "+", "-", "/", "*", "mod", "pow", "div": '))

operation_list = ["+", "-", "/", "*", "mod", "pow", "div"]

if z == operation_list[0]:
    print(x + y)
elif z == operation_list[1]:
    print(x - y)
elif z == operation_list[2] and y == 0:
    print("Деление на 0!")
elif z == operation_list[2] and y != 0:
    print(x / y)
elif z == operation_list[3]:
    print(x * y)
elif z == operation_list[4]:
    print(x % y)
elif z == operation_list[5]:
    print(x ** y)
elif z == operation_list[6]:
    print(x // y)
else:
    print("Введите корректную операцию из списка доступных операций")