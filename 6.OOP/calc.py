class Calculator():

    @staticmethod
    def summ(a: int, b: int) -> int:
        return a + b
    
class StringCalculator(Calculator):

    @staticmethod
    def summ(a: str | int, b: str | int) -> str | int:
        if type(a) == int and type(b) == int:
            return Calculator.summ(a, b)
        elif type(a) == str and type(b) == str:
            return a + b
        else:
            raise ValueError("Нельзя сложить строку с числом")
    
calc = Calculator()
str_calc = StringCalculator()
print(calc.summ(1, 2))
print(str_calc.summ("a", "b"))
print(str_calc.summ(3, 4))
print(str_calc.summ("a", 1))