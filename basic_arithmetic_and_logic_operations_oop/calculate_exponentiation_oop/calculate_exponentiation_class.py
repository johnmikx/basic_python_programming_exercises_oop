class CalculateExponentiation:
    def __init__(self):
        self.base = 0.0
        self.exponent = 0.0
        self.result = 0.0

    def get_input(self):
        self.base = float(input("Enter first number: "))
        self.exponent = float(input("Enter second number: "))

    def calculate(self):
        self.result = self.base ** self.exponent

    def display_output(self):
        print(f"{self.base} raised to {self.exponent} is: {self.result}")

    def execute(self):
        self.get_input()
        self.calculate()
        self.display_output()