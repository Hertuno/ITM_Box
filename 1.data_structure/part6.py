from typing import List
import main

def algorithm_binary_search(test_data: List[int]):
    
    algorithm_bubble_sort(test_data)
    # искомое число
    value = int(input("Введите искомое число: "))
    # индексы первого элемента, последнего и среднего
    low = 0
    high = len(test_data) - 1
    mid = len(test_data) // 2

    while test_data[mid] != value and low <= high:
        if value > test_data[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        print('Значение не найдено')
    else:
        print('Индекс найденного значения: ', mid)

    menu()

def algorithm_bubble_sort(test_data: List[int]):

    iterations = len(test_data) - 1
    for i in range(iterations):
        for j in range(iterations-i):
            if test_data[j] > test_data[j+1]:
                test_data[j], test_data[j+1] = test_data[j+1], test_data[j]

    print(f"Отсортированный список: {test_data}")

    menu()

def menu():

    test_data = [123, 25, 902, 234, 12, 2153, 1, 123, 0, 10, 0]
    print(f"Исходные данные: {test_data}")

    main_menu = {
        "1": "Часть 1: Бинарный поиск",
        "2": "Часть 2: Пузырьковая сортировка",
        "0": "Назад"
    }

    for key in main_menu:
        print(f"{key} - {main_menu[key]}")

    choice = input("Выберите пункт: ")

    if   choice == "1":  algorithm_binary_search(test_data)
    elif choice == "2":  algorithm_bubble_sort(test_data)
    elif choice == "0":  main.menu()
    else: menu()