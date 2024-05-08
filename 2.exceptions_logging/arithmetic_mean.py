import logging


def calculate_mean():
    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="a", encoding="utf-8")
    list_of_input = input("Введите список чисел:\n").split()
    list_of_number = []
    for item in list_of_input:
        try:
            list_of_number.append(int(item))
        except ValueError as e:
            logging.error(e)
            print(e)
    print(f"Среднее арифметическое: {sum(list_of_number) / len(list_of_number)}")


calculate_mean()
