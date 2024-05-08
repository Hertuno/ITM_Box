# Написать программу на Python для решения квадратного уравнения ax^2 + bx + c = 0.
# Если дискриминант отрицателен, программа должна выдать ошибку и предложить пользователю попробовать еще раз
# с другими коэффициентами. При выполнении скрипта в лог должна записываться информация о успехе или неудаче операции.
import logging


class OutOfRoot(Exception):
    """Исключение при отрицательном дискриминанте"""


def calculate():
    result = []
    a, b, c = input("Введите коофиценты a b c для уравнения: ax^2 + bx + c = 0\n").split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = b ** 2 - 4 * a * c
    if d == 0:
        result.append(-b / (2 * a))
    elif d > 0:
        result.append((-b + d ** 0.5) / (2 * a))
        result.append((-b - d ** 0.5) / (2 * a))
    elif d < 0:
        raise OutOfRoot("Уровнение не имеет корней, попробуйте еще раз с другими коофицентами")
    return result


def start():
    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="a", encoding="utf-8")
    try:
        roots = calculate()
    except Exception as e:
        logging.error(f"Неудача: {e}")
        print(e)
        start()
    else:
        logging.info("Успех")
        print(f"Найденые корни: {roots}")


start()
