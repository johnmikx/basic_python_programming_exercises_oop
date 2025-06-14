class FindLargerNumber:
    def __init__(self):
        self.num1 = 0.0
        self.num2 = 0.0
        self.larger = 0.0

    def get_input(self):
        self.num1 = float(input("Enter first number: "))
        self.num2 = float(input("Enter second number: "))

    def compare(self):
        self.larger = self.num1 if self.num1 > self.num2 else self.num2

    def display_output(self):
        print(f"{self.larger} is bigger.")

    def execute(self):
        self.get_input()
        self.compare()
        self.display_output()