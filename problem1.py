class Calculator:
    def addition(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b


name = Calculator()

print("Calculator")

while True:
    print('''Please select operation 
    1. Addition 
    2. Subtraction 
    3. Multiplication 
    4. Division
    5. Exit''')

    operations = int(input("Select operations from 1 to 5: "))
    if operations in (1, 2, 3, 4, 5):
        if operations == 5:
            break

        a = float(input("enter a: "))
        b = float(input("enter b: "))

        if operations == 1:
            print(f"{a} + {b} = {name.addition(a, b)}")

        elif operations == 2:
            print(f"{a} - {b} = {name.substract(a, b)}")

        elif operations == 3:
            print(f"{a} * {b} = {name.multiplication(a, b)}")

        elif operations == 4:
            print(f"{a} / {b} = {name.division(a, b)}")

    else:
        print("Invalid input")