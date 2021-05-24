class CalculatorStatic(object):
    def __init__(self):
        pass
    
    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second
    
    def div(self):
        return self.first / self.second

    @staticmethod
    def main():
        calc = CalculatorStatic(5, 2)
        print(f'{calc.first} + {calc.second} = {calc.add()}')
        print(f'{calc.first} + {calc.second} = {calc.sub()}')
        print(f'{calc.first} + {calc.second} = {calc.mul()}')
        print(f'{calc.first} + {calc.second} = {calc.div()}')
