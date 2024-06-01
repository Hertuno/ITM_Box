class Dog():
    __instance__ = None

    def __init__(self, name: str, age: int) -> None:
     
       if Dog.__instance__ is None: 
           Dog.__instance__ = self
           self.name = name
           self.age = age 
       else: 
           raise Exception("We can not creat another class") 
 
    @staticmethod 
    def get_instance(): 
        if not Dog.__instance__:
            Dog() 
        return Dog.__instance__ 
    
    def rename(self, new_name: str) -> None:
        self.name = new_name

    def grown_up(self) -> None:
        self.age += 1

    def info(self) -> str:
        return f"Меня зовут {self.name} и мне уже {self.age} лет"

    
 
dog = Dog("Бобик", 1) 
print(dog) 
 
same_dog = Dog.get_instance() 
print(same_dog) 
 
another_dog = Dog.get_instance() 
print(another_dog) 
 
#new_dog = Dog() 
#print(new_dog)

dog.rename("Боби")
dog.grown_up()
print(dog.info())  