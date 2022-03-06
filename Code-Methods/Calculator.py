class Calculator:

    def add(self, a, b):
        print(a + b)

    def multiply(self, a, b):
        return a * b


calculator = Calculator()

print('The sum of the two numbers are:')
calculator.add(2,5)

print('The Multiplication of the two numbers are: ')
print(calculator.multiply(2,5))

