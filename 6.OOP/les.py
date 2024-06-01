'''
класс принимает список людей с интерфейсом добавления новых 
и при итерации возвращал имена людей
'''
class List_of_people():
    peoples: list[str]
    iter_key: int

    def __init__(self, peoples: list[str] = None) -> None:
        self.peoples = peoples
        self._iter_key = 0

    def __iter__(self):
        return self

    def __next__(self):
        iter_key = self._iter_key
        if len(self.peoples) > iter_key:
            self._iter_key += 1
            return self.peoples[iter_key]               
        else:
            self._iter_key = 0
            raise StopIteration
    
    def add_peoples(self, peoples: list[str]) -> None:
        self.peoples += peoples

    def add_people(self, people: str) -> None:
        self.peoples.append(people)

people_list = List_of_people(['Denis', 'Maxim', 'Sergey'])
people_list.add_peoples(['Anton', 'Victor'])
people_list.add_people('Olga')
for name in people_list:
    print(name)
print(people_list.__next__())
 
'''
класс содерижит 3 любые атрибуты 
и при изменении логировать всё в консоль(при изменении старое->новое)
'''
import logging


def logged(cls):
    cls.log = logging.getLogger(cls.__name__)
    return cls

@logged
class Some_three_atr(): 
    x:int
    y:int
    xy_fun:str = 'x(y)'

    def __init__(self, x:int, y:int, xy_fun:str = ''):
        self.x = x
        self.y = y
        self.log.info(f"Создан экземпляр {self} с параметрами х:{x} y:{y}")

    def set_fun_atr(self, x:int, y:int):
        self.log.info(f"Атрибуты экземпляра {self} будут изменены")
        self.log.info(f"Старые значения х:{self.x} y:{self.y}")
        self.x = x
        self.y = y
        self.log.info(f"Новые значения х:{self.x} y:{self.y}")

    @classmethod
    def set_fun(cls, xy_fun:str):
        cls.log.info(f"Атрибут класса {cls.__name__} будут изменены")
        cls.log.info(f"Старые значения xy_fun:{cls.xy_fun}")
        cls.xy_fun = xy_fun
        cls.log.info(f"Новые значения xy_fun:{cls.xy_fun}")

logging.basicConfig(level=logging.INFO)
some_three = Some_three_atr(10, 5)
some_three_more = Some_three_atr(10, 5, 'x(y)')
some_three.set_fun_atr(9, 6)
some_three.set_fun('x * x - y = 0')
some_three_more.set_fun('x = y')
