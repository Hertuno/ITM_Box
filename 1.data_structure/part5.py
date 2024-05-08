import main

def create_dict():
    name = input("Введите имя: ")
    age = input("Введите возраст: ")
    sex = input("Введите пол: ")
    height = input("Введите рост: ")
    weight = input("Введите вес: ")
    legs = input("Введите размер ноги: ")
    dict = {
        "name": name,
        "age": age,
        "sex": sex,
        "height": height,
        "weight": weight,
        "legs": legs
    }
    print(dict)
    menu()

def show_dict():
    dict = {
        "name": "Имя",
        "age": "Возраст",
        "sex": "Пол",
        "height": "Рост",
        "weight": "Вес",
        "legs": "Размер ноги"
    }
    print(dict)
    menu()

def add_dict():
    name = input("Введите имя: ")
    age = input("Введите возраст: ")
    sex = input("Введите пол: ")
    height = input("Введите рост: ")
    weight = input("Введите вес: ")
    legs = input("Введите размер ноги: ")
    dict = {
        "name": name,
        "age": age,
        "sex": sex,
        "height": height,
        "weight": weight,
        "legs": legs
    }
    print(dict)
    menu()

def del_dict():
    name = input("Введите имя: ")
    dict = {
        "name": name
    }
    print(dict)
    menu()

def menu():
    main_menu = {
        "1": "Создайте словарь содержащий данные о человеке. В качестве строковых ключей используйте его имя, возраст, пол, рост, вес, размер ноги.",
        "2": "Выведите на экран все данные о человеке по ключам.",
        "3": "Добавьте в словарь ключ и значение размера ноги",
        "4": "Удалите из словаря возраст.",
        "0": "Назад"
    }

    for key in main_menu:
        print(f"{key} - {main_menu[key]}")

    choice = input("Выберите пункт: ")

    if   choice == "1": create_dict()
    elif choice == "2": show_dict()
    elif choice == "3": add_dict()
    elif choice == "4": del_dict()
    elif choice == "0": main.menu()
    else: menu()