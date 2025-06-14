class PrintOddNumbersToHundred:
    def __init__(self):
        self.numbers = []

    def generate_numbers(self):
        num = 1
        while num <= 100:
            self.numbers.append(num)
            num += 2

    def display_output(self):
        print(*self.numbers)

    def execute(self):
        self.generate_numbers()
        self.display_output()