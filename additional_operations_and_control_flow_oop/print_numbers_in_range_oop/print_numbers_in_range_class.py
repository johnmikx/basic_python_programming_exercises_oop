class PrintNumbersInRange:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.numbers = []

    def get_input(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))

    def generate_numbers(self):
        start, end = (self.num1, self.num2) if self.num1 <= self.num2 else (self.num2, self.num1)
        self.numbers = list(range(start + 1, end))

    def display_output(self):
        print(f"Numbers between {self.num1} and {self.num2}:")
        print(*self.numbers)

    def execute(self):
        self.get_input()
        self.generate_numbers()
        self.display_output()