"""
1. Даны три целых числа. Найти количество положительных чисел в исходном наборе.
"""
input_strings = input("Введите числа").split()
input_numbers = [int(item) for item in input_strings]
positive_count = 0
for numer in input_numbers:
    if numer >= 0:
        positive_count += 1
print(f"Количество положительных чисел: {positive_count}")
"""
2. Даны два числа. Вывести большее из них.
"""
first_number = int(input("Введите первое число"))
second_number = int(input("Введите второе число"))
if first_number > second_number:
    print(first_number)
else:
    print(second_number)
"""
3. Даны два числа. Вывести вначале большее, а затем меньшее из них.
"""
first_number = int(input("Введите первое число"))
second_number = int(input("Введите второе число"))
if first_number > second_number:
    print(first_number, second_number)
else:
    print(second_number, first_number)
"""
4. Даны три числа. Найти наименьшее из них.
"""
first_number = int(input("Введите первое число"))
second_number = int(input("Введите второе число"))
third_number = int(input("Введите третье число"))
if first_number < second_number and first_number < third_number:
    print(first_number)
elif second_number < first_number and second_number < third_number:
    print(second_number)
else:
    print(third_number)
"""
5. Даны координаты точки, не лежащей на координатных осях OX и OY. 
Определить номер координатной четверти, в которой находится данная точка. 
Координаты задаются пользователем, например (10, 15).
II | I
---0---
III| IV
"""
x_number = int(input("Введите X"))
y_number = int(input("Введите Y"))
if x_number > 0 and y_number > 0:
    quarter = "I"
elif x_number > 0 > y_number:
    quarter = "IV"
elif x_number < 0 < y_number:
    quarter = "II"
elif x_number < 0 and y_number < 0:
    quarter = "III"
else:
    quarter = None

if quarter is None:
    print("Точка лежит на координатной оси")
else:
    print(f"Номер координатной четверти: {quarter}")



