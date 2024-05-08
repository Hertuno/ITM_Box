import logging
import random


class RangeBordersUnderZero(Exception):
    """Исключение если граница меньше 0"""


def generate_number():
    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="a", encoding="utf-8")
    start, stop = input("Введите границы для генерации случайного числа\n").split()
    try:
        start, stop = int(start), int(stop)
    except ValueError as e:
        logging.error(e)
        print("Попробуйте еще раз")
        generate_number()
    try:
        if start < 0 or stop < 0:
            raise RangeBordersUnderZero("Граница меньше 0")
        else:
            print(f"Случайное число: {random.randrange(int(start), int(stop))}")
    except Exception as e:
        logging.error(e)
        print("Попробуйте еще раз")
        generate_number()


generate_number()
