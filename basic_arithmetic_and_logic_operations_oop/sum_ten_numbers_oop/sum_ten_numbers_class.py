class SumTenNumbers:
    def __init__(self):
        self.numbers = []
        self.total = 0.0

    def get_input(self):
        for i in range(10):
            num = float(input(f"Enter number {i+1}: "))
            self.numbers.append(num)

    def calculate(self):
        self.total = sum(self.numbers)

    def display_output(self):
        print(f"The sum of all numbers is: {self.total}")

    def execute(self):
        self.get_input()
        self.calculate()
        self.display_output()