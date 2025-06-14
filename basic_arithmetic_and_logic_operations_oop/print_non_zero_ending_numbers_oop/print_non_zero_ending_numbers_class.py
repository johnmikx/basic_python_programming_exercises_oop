class PrintNonZeroEndingNumbers:
    def __init__(self):
        self.numbers = []

    def generate_numbers(self):
        self.numbers = [num for num in range(0, 101) if num % 10 != 0]

    def display_output(self):
        print("Numbers from 0 to 100 except those ending in zero:")
        print(*self.numbers)

    def execute(self):
        self.generate_numbers()
        self.display_output()