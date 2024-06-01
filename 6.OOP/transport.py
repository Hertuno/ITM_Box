from typing import Self


class MeansOfTransport:
    
    def __init__(self, brand:str, color:str) -> None:
        self.__brand = brand
        self.__color = color

    def show_brand(self) -> None:
        print(self.__brand)
    
    def show_color(self) -> None:
        print(self.__color)

    def get_brand(self) -> str:
        return self.__brand

    def get_color(self) -> str:
        return self.__color
    
    def set_brand(self, brand:str) -> None:
        self.__brand = brand

    def set_color(self, color:str) -> None:
        self.__color = color

class Car(MeansOfTransport):
    fuel = 100
    cur_speed = 260
    _fuel_spend = 19
    __cur_fuel_spend = 10
    car_drive = 4
    __car_state = "отличное"

    def __new__(cls, *args, **kwargs) -> Self:
        return super().__new__(cls)
    
    def __init__(self, brand: str, color: str, wheel_len: float) -> None:
        super().__init__(brand, color)
        self.__wheel_len = wheel_len

    def __del__(self) -> None:
        del self

    def __str__(self) -> str:
        return f"Топливо {self.fuel}, скорость {self.cur_speed}, состояние {self.__car_state}"

    def __eq__(self, other) -> bool:
        return self.get_brand() == other.get_brand() and self.get_color() == other.get_color()

    def __ne__(self, other) -> bool:
        return self.get_brand() != other.get_brand() or self.get_color() != other.get_color()

    def __lt__(self, other) -> bool:
        return self.get_wheel() < other.get_wheel()

    def __gt__(self, other) -> bool:
        return self.get_wheel() > other.get_wheel()

    def __le__(self, other) -> bool:
        return self.get_wheel() <= other.get_wheel()

    def __ge__(self, other) -> bool:
        return self.__wheel_len >= other.get_wheel()

    def __pos__(self) -> str:
        self.__car_state = "после дтп"
        return self

    def __neg__(self) -> None:
        self.__car_state = "украденая"
        return self

    def __abs__(self) -> Self:
        self.__car_state = "существует"
        return self

    def __invert__(self) -> Self:
        self.__car_state = "перевёртыш"
        return self

    def __round__(self, n) -> Self:
        self.__car_state = f"перевернулась %1 раз", n
        return self

    def __floor__(self) -> Self:
        self.__wheel_len = 0 if self.__wheel_len < 4 else 4
        return self

    def __ceil__(self) -> Self:
        self.__wheel_len = 8 if self.__wheel_len > 4 else 4
        return self

    def __trunc__(self) -> Self:
        self.__wheel_len = self.__wheel_len // 1
        return self
    
    def __add__(self, other) -> list:
        return list(self, other)
    
    def __sub__(self, other) -> None:
        return None
    
    def __mul__(self, other) -> int:
        return 1
        
    @staticmethod
    def travel_time(distance: float, max_speed: float) -> float:
        return distance / max_speed
    
    @classmethod
    def get_wheel(self) -> float:
        return self.__wheel_len
    
    @classmethod
    def get_car_state(self) -> str:
        return self.__car_state

    @classmethod
    def show_car_drive() -> None:
        print(Car.car_drive)

class Moped(MeansOfTransport):

    def __init__(self, brand: str, color: str, wheel_len: int) -> None:
        super().__init__(brand, color)
        self.__wheel_len = wheel_len

mot = MeansOfTransport('Toyota', 'Black')
mot.show_brand()
mot.show_color()
mot.set_brand('Mazda')
mot.set_color('Red')

carx = Car("brand1", "color1", 3)
cary = Car("brand2", "color2", 5)
carz = Car("brand1", "color1", 10)

#print(f"Состояние {carz.__car_state}")
print(f"Состояние {carz.get_car_state()}")
print(f"Расход топлива {carz._fuel_spend}")

print(f"carx = cary: {carx == cary}")
print(f"carx = carz: {carx == carz}")
print(+carx)
print(-cary)