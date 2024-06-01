"""класс принимает список людей с интерфейсом добавления новых и при итерации возвращал имена людей"""


class List_of_people:
    peoples: list[str]

    def __init__(self, peoples: list[str] = None) -> None:
        self.peoples = peoples

    def __iter__(self):
        self._iter_key = 0
        return self

    def __next__(self):
        iter_key = self._iter_key
        if len(self.peoples) > iter_key:
            self._iter_key += 1
            return self.peoples[iter_key]
        else:
            raise StopIteration

    def add_peoples(self, peoples: list[str]) -> None:
        self.peoples += peoples

    def add_people(self, people: str) -> None:
        self.peoples.append(people)


people_list = List_of_people(["Denis", "Maxim", "Sergey"])
people_list.add_peoples(["Anton", "Victor"])
people_list.add_people("Olga")
for name in people_list:
    print(name)
print(people_list.__next__())

"""класс содерижит 3 любые атрибуты и при изменении логировать всё в консоль(при изменении старое->новое)"""
import logging


def logged(cls):
    cls.log = logging.getLogger(cls.__name__)
    return cls


@logged
class Some_three_atr:

    def __init__(self, x: int, y: int):
        self.__xy_fun = "x(y)"
        self.__x = x
        self.__y = y
        self.log.info(f"Создан экземпляр {self} с параметрами х:{x} y:{y}")

    @property
    def xy_atr(self) -> tuple:
        return (self.__x, self.__y)

    @xy_atr.setter
    def xy_atr(self, atr: tuple[int]):
        x, y = atr
        self.log.info(f"Атрибуты экземпляра {self} будут изменены")
        self.log.info(f"Старые значения х:{self.__x} y:{self.__y}")
        self.__x = x
        self.__y = y
        self.log.info(f"Новые значения х:{self.__x} y:{self.__y}")

    @property
    def xy_fun(self) -> str:
        return self.__xy_fun

    @xy_fun.setter
    def xy_fun(self, xy_fun: str):
        self.log.info(f"Атрибут класса {self} будут изменены")
        self.log.info(f"Старые значения xy_fun:{self.__xy_fun}")
        self.__xy_fun = xy_fun
        self.log.info(f"Новые значения xy_fun:{self.__xy_fun}")


logging.basicConfig(level=logging.INFO)
three_atr_one = Some_three_atr(9, 4)
three_atr_two = Some_three_atr(10, 5)
three_atr_one.xy_atr = 1, 2
three_atr_one.xy_fun = "x * x - y = 0"
three_atr_two.xy_atr = 4, 1
three_atr_two.xy_fun = "x = y"
