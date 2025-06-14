class CountEvenNumbers:
    def __init__(self):
        self.numbers = []
        self.even_count = 0

    def get_input(self):
        for i in range(10):
            num = int(input(f"Enter number {i+1}: "))
            self.numbers.append(num)

    def count(self):
        self.even_count = sum(1 for num in self.numbers if num % 2 == 0)

    def display_output(self):
        print(f"The count of even numbers is: {self.even_count}")

    def execute(self):
        self.get_input()
        self.count()
        self.display_output()