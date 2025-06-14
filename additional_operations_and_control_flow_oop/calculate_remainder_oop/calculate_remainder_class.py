class CalculateRemainder:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.remainder = None

    def get_input(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))

    def calculate(self):
        if self.num2 == 0:
            self.remainder = "undefined"
        else:
            self.remainder = self.num1 % self.num2

    def display_output(self):
        print(f"The remainder is: {self.remainder}")

    def execute(self):
        self.get_input()
        self.calculate()
        self.display_output()