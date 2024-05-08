from math import pi
"""
3. Напишите программу для подсчета среднего числа всех введенных пользователям чисел.
Ввод пользователя должен осуществляться с помощью input. Если пользователь вводит ноль,
то выводиться на экран среднее значение. Используйте цикл while для решения данной задачи
"""
summ = count = 0
while input_string := int(input("Введите число: ")) != 0:
    count += 1
    summ += input_string
print(f"Среднее арифметическое списка равно: {summ / count}")
"""
4. Напишите программу для вывода на экран чисел от 0 до 100
Вам понадобиться цикл for, конструкция range и print
"""
for i in range(100, 0, -1):
    print(i)
"""
5. Напишите программу для вывода таблицы умножения от 0 до 9. 
Используйте вложенный цикл for, print и range
Пример:
0*1 = 0
0 *2 = 0
…..
9*1 = 9
9*2=18
"""
[[print(f"{i}*{j}={i*j}") for j in range(10)] for i in range(10)]

[print(f"{i}*{j}={i*j}") for i in range(10) for j in range(10)]

for i in range(10):
    for j in range(10):
        print(f"{i}*{j}={i*j}")
"""
6. Создайте список с разными значениями, пройдитесь по нему в цикле и выведите на экран. 
(Сделайте тоже самое со словарем и выведите ключ и значение)
"""
some_list = [str(round(pi, i)) for i in range(1, 6)]
some_dict = {num: num**2 for num in range(1, 11)}
for some_number in some_list:
    print(some_number)
for some_item in some_dict.items():
    print(some_item[0], some_item[1])
"""
7. Вывести все числа от 1 до 100, которые делятся на 3 без остатка.
"""
for i in range(1, 101):
    if i % 3 == 0:
        print(i)
"""
8. Найти сумму всех чисел от 1 до 100
"""
sum_hungred = 0
for i in range(101):
    sum_hungred += i
print(sum_hungred)
"""
9. Вывести таблицу умножения для числа 2 от 1 до 10.
"""
for i in range(1, 11):
    print(f"2*{i}={i+i}")
"""
10. Найти все простые числа от 2 до 50.
"""
easy_numbers = []
for i in range(2, 51):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        easy_numbers.append(i)
print(easy_numbers)
"""
11. Посчитать сумму квадратов чисел от 1 до 10.
"""
result = 0
for i in range(1, 11):
    result += i**2
print(result)
"""
12. Вывести значения функции y=x^2 от 1 до 10 с шагом 0.5.
"""
result = []
for x in range(5, 105, 5):
    result.append((x/10)**2)
print(result)
# или
result = []
for x in range(1, 11):
    result.append((x-0.5)**2)
    result.append(x**2)
print(result)
"""
13. Найти факториалы чисел от 1 до 5 (включительно).
"""
for i in range(1, 6):
    current_factorial = 1
    for j in range(1, i + 1):
        current_factorial *= j
    print(f"Факториал {i} = {current_factorial}")
