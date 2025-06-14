class CalculateIntegerQuotient:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.quotient = None

    def get_input(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))

    def calculate(self):
        if self.num2 == 0:
            self.quotient = "undefined"
        else:
            self.quotient = self.num1 // self.num2

    def display_output(self):
        print(f"The quotient is: {self.quotient}")

    def execute(self):
        self.get_input()
        self.calculate()
        self.display_output()