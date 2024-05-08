from typing import List
import main

def first_third_and_cut(list_a: List[int]):
    print(list_a[0], list_a[2], list_a[3:])
    menu()

def plus_to_minus_and_cityname(list_a: List[str]):
    cityname = ""
    for i in range(len(list_a)):
        if list_a[i] == "+": list_a[i] = "-"
        cityname.join(list_a[i])
    print(cityname)
    menu()

def only_letters_and_only_numbers(list_a: List[str]) -> List[str]:
    list_alpha = []
    list_digit = []
    for i in range(len(list_a)):
        if list_a[i].isalpha(): list_alpha.append(list_a[i])
        if list_a[i].isdigit(): list_digit.append(list_a[i])
    print(list_alpha, list_digit)
    menu()
    return list_alpha

def delete_and_reverse(list_a: List[int]):
    list_a.remove(1)
    list_a.reverse()
    print(list_a)
    menu()

def list_to_set(list_a: List[int]):
    list_a = set(list_a)
    print(list_a)
    menu()

def menu():

    income_data = {
        "1": [1, 2, 3 ,4 ,5],
        "2": ["Ростов", "+", "на", "-", "Дону"],
        "3": ["a", "s", "1", "a", "32", "23"],
        "4": ["a", "s", "1", "a", "32", "23"],
        "5": ["a", "s", "1", "a", "32", "23"]
    }

    main_menu = {
        "1": f"Используя операции индексирования и среза выведите на экран первый и третий элементы списка {income_data['1']}, а также срез списка из первых трех элементов.",
        "2": f"Дан список {income_data['2']}. Исправьте плюс на дефис и выведите название города на экран использовав доступ к элементам списка по индексам",
        "3": f"Дан список {income_data['3']}. Разбейте его на два списка: только с буквами и только с числами.",
        "4": "В предыдущей задаче должен был получиться список из букв. Используя методы списков: удалите из него последний элемент, сделайте реверсию списка.",
        "5": f"Преобразуйте список {income_data['3']} в set и выведите на экран. Что изменилось?",
        "0": "Назад"
    }
    
    for key in main_menu:
        print(f"{key} - {main_menu[key]}")

    choice = input("Выберите пункт: ")
    
    if   choice == "1":  first_third_and_cut(income_data[choice])
    elif choice == "2":  plus_to_minus_and_cityname(income_data[choice])
    elif choice == "3":  _ = only_letters_and_only_numbers(income_data[choice])
    elif choice == "4":  delete_and_reverse(only_letters_and_only_numbers(income_data[choice]))
    elif choice == "5":  list_to_set(income_data[choice])
    elif choice == "0": main.menu()
    else: menu()