import main

def square_perimeter():
    a = input("Введите сторону квадрата: ")
    print(f"Периметр квадрата: {4*a}")
    menu()

def square_area():
    a = input("Введите сторону квадрата: ")
    print(f"Площадь квадрата: {a*2}")
    menu()

def rectangle_perimeter_and_area():
    a = input("Введите первую сторону прямоугольника: ")
    b = input("Введите вторую сторону прямоугольника: ")
    print(f"Периметр прямоугольника: {2*(a + b)}")
    print(f"Площадь прямоугольника: {a*b}")
    menu()

def circle_length():
    p = 3.14
    d = input("Введите диаметр окружности: ")
    print(f"Длина окружности: {p*d}")
    menu()

def cube_volume_and_surface_area():
    a = input("Введите длину ребра куба: ")
    print(f"Объем куба: {a*3}")
    print(f"Площадь поверхности куба: {6*a*2}")
    menu()

def rectangular_prism_volume_and_surface_area():
    a = input("Введите первую длину ребра прямоугольного параллелепипеда: ")
    b = input("Введите вторую длину ребра прямоугольного параллелепипеда: ")
    c = input("Введите третью длину ребра прямоугольного параллелепипеда: ")
    print(f"Объем прямоугольного параллелепипеда: {a*b*c}")
    print(f"Площадь поверхности прямоугольного параллелепипеда: {2*(a*b + b*c + a*c)}")
    menu()

def circle_radius_and_area():
    p = 3.14
    r = input("Введите радиус окружности: ")
    print(f"Длина окружности: {2*p*r}")
    print(f"Площадь круга: {p*r*r}")
    menu()

def arithmetic_mean():
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    print(f"Среднее арифметическое: {(a + b)/2}")
    menu()

def geometric_mean():
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    print(f"Среднее геометрическое: {(a*b)**(1/2)}")
    menu()

def arithmetic_mean_and_geometric_mean():
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    print(f"Среднее арифметическое: {(a + b)/2}")
    print(f"Среднее геометрическое: {(a*b)**(1/2)}")
    menu()

def back_to_main():
    main.main()

def menu():
    main_menu = {
        "1":  "Дана сторона квадрата a. Найти его периметр P = 4*a",
        "2":  "Дана сторона квадрата a. Найти его площадь S = a*2",
        "3":  "Даны стороны прямоугольника a и b. Найти его площадь S = a*b и периметр P = 2*(a + b)",
        "4":  "Дан диаметр окружности d. Найти ее длину L = π*d, π = 3.14",
        "5":  "Дана длина ребра куба a. Найти объем куба V = a*3 и площадь его поверхности S = 6*a*2",
        "6":  "Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти его объем V = a*b*c и площадь поверхности S = 2*(a*b + b*c + a*c)",
        "7":  "Найти длину окружности L и площадь круга S заданного радиуса R: L = 2*π*R, S = π*R*2, π=3.14",
        "8":  "Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2",
        "9":  "Даны два неотрицательных числа a и b. Найти их среднее геометрическое, т. е. квадратный корень из их произведения: (a*b)**1/2",
        "10": "Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.",
        "0":  "Назад"
    }

    for key in main_menu:
        print(f"{key} - {main_menu[key]}")

    choice = input("Выберите пункт: ")

    if choice in main_menu:
        print(main_menu[choice])
    else:
        print("Такой задачи нет")

    if   choice == "0":  back_to_main()
    elif choice == "1":  square_area()
    elif choice == "2":  square_perimeter()
    elif choice == "3":  rectangle_perimeter_and_area()
    elif choice == "4":  circle_length()()
    elif choice == "5":  cube_volume_and_surface_area()
    elif choice == "6":  rectangular_prism_volume_and_surface_area()
    elif choice == "7":  circle_radius_and_area()
    elif choice == "8":  arithmetic_mean()
    elif choice == "9":  geometric_mean()
    elif choice == "10": arithmetic_mean_and_geometric_mean()
    else: menu()