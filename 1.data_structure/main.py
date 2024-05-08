import part1, part2, part3, part4, part5, part6

def menu():
    main_menu = {
        "1": "Часть 1: Базовые арифметические операции",
        "2": "Часть 2: Деление нацело и нахождение остатка",
        "3": "Часть 3:",
        "4": "Часть 4:",
        "5": "Часть 5:",
        "6": "Часть 6:",
        "0": "Выход"
    }

    for key in main_menu:
        print(f"{key} - {main_menu[key]}")

    choice = input("Выберите пункт: ")

    if   choice == "0": exit()
    elif choice == "1": part1.menu()
    elif choice == "2": part2.menu()
    elif choice == "3": part3.menu()
    elif choice == "4": part4.menu()
    elif choice == "5": part5.menu()
    elif choice == "6": part6.menu()
    else: menu()
    
menu()