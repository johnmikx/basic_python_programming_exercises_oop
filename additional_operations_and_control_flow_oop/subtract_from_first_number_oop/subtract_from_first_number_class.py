class SubtractFromFirstNumber:
    def __init__(self):
        self.first_number = 0.0
        self.numbers = []
        self.result = 0.0

    def get_input(self):
        self.first_number = float(input("Enter the first number: "))
        self.result = self.first_number
        for i in range(9):
            num = float(input(f"Enter number {i+2}: "))
            self.numbers.append(num)

    def calculate(self):
        self.result -= sum(self.numbers)

    def display_output(self):
        print(f"The result of {self.first_number} minus all other numbers is: {self.result}")

    def execute(self):
        self.get_input()
        self.calculate()
        self.display_output()