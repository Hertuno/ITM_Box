class Animal():
    weight: int
    height: int

class Duck(Animal):
    def __init__(self, weight: int, height: int) -> None:
        self.weight = weight
        self.height = height

    @setattr
    def set_height(self, new_height: int):
        self.height = new_height

    

duck1 = Duck(10, 2)
duck1.set_height(20)
duck1.height = 10
print(duck1.weight, duck1.height)
