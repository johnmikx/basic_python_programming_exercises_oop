class CalculateProduct:
    def __init__(self):
        self.num1 = 0.0
        self.num2 = 0.0
        self.product = 0.0

    def get_input(self):
        self.num1 = float(input("Enter first number: "))
        self.num2 = float(input("Enter second number: "))

    def calculate(self):
        self.product = self.num1 * self.num2

    def display_output(self):
        print(f"The product is: {self.product}")

    def execute(self):
        self.get_input()
        self.calculate()
        self.display_output()