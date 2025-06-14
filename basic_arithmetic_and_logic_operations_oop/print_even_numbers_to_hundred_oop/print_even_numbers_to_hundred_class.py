class PrintEvenNumbersToHundred:
    def __init__(self):
        self.numbers = []

    def generate_numbers(self):
        self.numbers = list(range(0, 101, 2))

    def display_output(self):
        print("Even numbers from 0 to 100:")
        print(*self.numbers)

    def execute(self):
        self.generate_numbers()
        self.display_output()