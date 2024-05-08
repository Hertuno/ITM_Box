"""
1.Дано целое число K. Вывести строку-описание оценки, соответствующей числу K
(1 — «плохо», 2 — «неудовлетворительно», 3 — «удовлетворительно», 4 — «хорошо», 5 — «отлично»).
Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».
"""
k_number = int(input("Введите целое число K"))
match k_number:
    case 1:
        print("плохо")
    case 2:
        print("неудовлетворительно")
    case 3:
        print("удовлетворительно")
    case 4:
        print("хорошо")
    case 5:
        print("отлично")
    case _:
        print("ошибка")
"""
2. Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 — февраль и т. д.). 
Определить количество дней в этом месяце для невисокосного года.
"""
month_number = int(input("Введите номер месяца"))
match month_number:
    case 1:
        print("В январе 31 день")
    case 2:
        print("В феврале 28 дней")
    case 3:
        print("В марте 31 день")
    case 4:
        print("В апреле 30 день")
    case 5:
        print("В мае 31 день")
    case 6:
        print("В июне 30 день")
    case 7:
        print("В июле 31 день")
    case 8:
        print("В августе 31 день")
    case 9:
        print("В сентябре 30 день")
    case 10:
        print("В октябре 31 день")
    case 11:
        print("В ноябре 30 день")
    case 12:
        print("В декабе 31 день")
    case _:
        print("неверный номер месяца")
"""
3. Даны два целых числа: D (день) и M (месяц), определяющие правильную дату невисокосного года. 
Вывести значения D и M для даты, следующей за указанной.
"""
next_day = "Следующий месяц и день: {}/{}"
match mounth := int(input("Введите месяц")):
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        if day := int(input("Введите день")) == 31:
            if mounth == 12:
                print(next_day.format(1, 1))
            else:
                print(next_day.format(1, mounth + 1))
        else:
            print(next_day.format(day + 1, mounth))
    case 4 | 6 | 9 | 11:
        if day := int(input("Введите день")) == 30:
            print(next_day.format(1, mounth + 1))
        else:
            print(next_day.format(day + 1, mounth))
    case 2:
        if day := int(input("Введите день")) == 28:
            print(next_day.format(1, mounth + 1))
        else:
            print(next_day.format(day + 1, mounth))
"""
4. Робот может перемещаться в четырех направлениях («С» — север, «З» — запад, «Ю» — юг, «В» — восток) 
и принимать три цифровые команды: 0 — продолжать движение, 1 — поворот налево, −1 — поворот направо. 
Дан символ C — исходное направление робота и целое число N — посланная ему команда. 
Вывести направление робота после выполнения полученной команды.
"""
print("0 — продолжать движение, 1 — поворот налево, −1 — поворот направо.")
way = "С"
while True:
    command = int(input("Введите команду: "))
    if command == 1:
        match way:
            case "С":
                way = "З"
            case "З":
                way = "Ю"
            case "Ю":
                way = "В"
            case "В":
                way = "С"
        print(f"Сменил направление движения: {way}")
    elif command == -1:
        match way:
            case "С":
                way = "В"
            case "З":
                way = "С"
            case "Ю":
                way = "З"
            case "В":
                way = "Ю"
        print(f"Сменил направление движения: {way}")
    elif command == 0:
        print(f"Продолжаю движение по направлению: {way}")
    else:
        break
"""
5. Дано целое число в диапазоне 100–999. Вывести строку-описание данного числа, 
например: 256 — «двести пятьдесят шесть», 814 — «восемьсот четырнадцать».
"""
number = int(input("Введите целое число в диапозоне 100-999"))
numer_about = ""
if numer_about in range(100, 1000):
    match number // 100:
        case 1:
            numer_about += "сто "
        case 2:
            numer_about += "двести "
        case 3:
            numer_about += "триста "
        case 4:
            numer_about += "четыреста "
        case 5:
            numer_about += "пятьсот "
        case 6:
            numer_about += "шестьсот "
        case 7:
            numer_about += "семьсот "
        case 8:
            numer_about += "восемьсот "
        case 9:
            numer_about += "девятьсот "
else:
    pass
if number % 100 // 10 == 1:
    match number % 100:
        case 10:
            numer_about += "десять"
        case 11:
            numer_about += "одинадцать"
        case 12:
            numer_about += "двенадцать"
        case 13:
            numer_about += "тринадцать"
        case 14:
            numer_about += "четырнадцать"
        case 15:
            numer_about += "пятнадцать"
        case 16:
            numer_about += "шестнадцать"
        case 17:
            numer_about += "семнадцать"
        case 18:
            numer_about += "восемнадцать"
        case 19:
            numer_about += "девятнадцать"
else:
    match number % 100 // 10:
        case 2:
            numer_about += "двадцать "
        case 3:
            numer_about += "тридцать "
        case 4:
            numer_about += "сорок "
        case 5:
            numer_about += "пятьдесят "
        case 6:
            numer_about += "шестьдесят "
        case 7:
            numer_about += "семьдесят "
        case 8:
            numer_about += "восемьдесят "
        case 9:
            numer_about += "девяносто "
    match number % 10:
        case 1:
            numer_about += "один"
        case 2:
            numer_about += "два"
        case 3:
            numer_about += "три"
        case 4:
            numer_about += "четыре"
        case 5:
            numer_about += "пять"
        case 6:
            numer_about += "шесть"
        case 7:
            numer_about += "семь"
        case 8:
            numer_about += "восемь"
        case 9:
            numer_about += "девять"
print(numer_about)
"""
6. *** Реализуйте программу калькулятор. 
На вход подается три значения: первое число, второе число и операция( *, /, + или -) . 
На выходе должны получить число, после выполнения операции.
"""
input_data = input("На вход подается три значения: первое число, второе число и операция( *, /, + или -)").split()
first_number = int(input_data[0])
second_number = int(input_data[1])
match input_data[2]:
    case "*":
        print(f"Результат умножения: {first_number * second_number}")
    case "/":
        print(f"Результат деления: {first_number / second_number}")
    case "+":
        print(f"Результат сложения: {first_number + second_number}")
    case "-":
        print(f"Результат вычитания: {first_number - second_number}")
