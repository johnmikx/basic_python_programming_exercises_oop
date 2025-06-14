class CheckNotEqualNumbers:
    def __init__(self):
        self.num1 = 0.0
        self.num2 = 0.0
        self.result = ""

    def get_input(self):
        self.num1 = float(input("Enter first number: "))
        self.num2 = float(input("Enter second number: "))

    def check(self):
        self.result = "Not Equal" if self.num1 != self.num2 else "Equal"

    def display_output(self):
        print(self.result)

    def execute(self):
        self.get_input()
        self.check()
        self.display_output()