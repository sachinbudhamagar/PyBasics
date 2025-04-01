#OOP CONCEPTS ON CALCULATOR
# Object-Oriented Programming (OOP) concepts in Python


"""import math

# Base class for calculator operations
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

# Derived class for advanced calculator operations (Inheritance)
class AdvancedCalculator(Calculator):
    def percentage(self, a, b):
        if b != 0:
            return (a / b) * 100
        else:
            return "Cannot calculate percentage with zero as denominator"

    def square_root(self, a):
        if a >= 0:
            return math.sqrt(a)
        else:
            return "Cannot calculate square root of a negative number"

    def power(self, a, b):
        return a ** b

# Encapsulation: User interaction handled by this class
class CalculatorApp:
    def __init__(self):
        self.calculator = AdvancedCalculator()  # Composition: Using AdvancedCalculator

    def display_menu(self):
        print("Welcome to the Advanced Calculator!")
        print("-" * 30)
        print("Available operations:")
        print(" +  : Addition")
        print(" -  : Subtraction")
        print(" *  : Multiplication")
        print(" /  : Division")
        print(" %  : Percentage")
        print(" ** : Power (e.g., a^b)")
        print(" ^  : Square root (only first number is used)")
        print(" x  : Exit")
        print("-" * 30)

    def perform_operation(self):
        while True:
            operation = input("Choose an operation (+, -, *, /, %, **, ^, x): ").lower()

            if operation == "x":
                print("Thank you for using the calculator. Goodbye!")
                break

            if operation == "^":
                a = float(input("Enter the number: "))
                result = self.calculator.square_root(a)
                print(f"Result: {result}")
                continue

            elif operation == "**":
                a = float(input("Enter the base number: "))
                b = float(input("Enter the exponent: "))
                result = self.calculator.power(a, b)
                print(f"Result: {result}")
                continue

            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            if operation == "+":
                result = self.calculator.add(a, b)
            elif operation == "-":
                result = self.calculator.subtract(a, b)
            elif operation == "*":
                result = self.calculator.multiply(a, b)
            elif operation == "/":
                result = self.calculator.divide(a, b)
            elif operation == "%":
                result = self.calculator.percentage(a, b)
            else:
                print("Invalid operation. Please try again.")
                continue

            print(f"Result: {result}")
            print("-" * 30)

# Main program to run the calculator
if __name__ == "__main__":
    app = CalculatorApp()  # Create an instance of CalculatorApp
    app.display_menu()     # Show the menu
    app.perform_operation()  # Start the calculator
"""

import math
class calcu:
    def add(self, a, b):
        return a + b
    
    def sub (self, a, b):
        return a - b

    def mul (self, a, b):
        return a * b
    
    def div (self, a, b):
        if b != 0:
            return a / b
        else:
            return ("Unable to divide by 0")

class AdvanceCalcu(calcu):
    def percent (self, a, b):
        return a / b * 100
    
    def squrt (self, a):
        if a >= 0:
            return math.sqrt(a)
        else:
            return ("Error with 0! Enter valid no.")
    
    def squre (self, a, b):
        return a**b

class calculator:
    def __init__ (self):
        self.calculator = AdvanceCalcu()

    def menu(self):
        print ("Welcome to simple calculator")
        print ('_' * 30)
        print ("'+' : Addation")
        print ("'-' : Subtraction")
        print ("'*' : Multiplication")
        print ("'/' : Division")
        print ("'^' : Square Root")
        print ("'**' : Square")
        print ("'%' : percentage")
        print ('_' * 30)

    def operation (self):
        while True:
            try:

                operation = input("Choose your operation ( +, -, *, /, %, **, ^, x:) ").lower()
                
                if operation == "x":
                    print("Thank you for your visit.")
                    print ('_' * 30)
                    break
                

                if operation == "^":
                    a = float(input("Enter no.1: "))
                    result = self.calculator.squrt(a)
                    print(f"Result: {result}")
                    print ('_' * 30)
                    continue

                elif operation == "**":
                    a = float(input("Enter no.1: "))
                    b = float(input("Enter no.2: "))
                    result = self.calculator.squre(a,b)
                    print(f"Result: {result}")
                    print ('_' * 30)
                    continue

                a = float(input("Enter no.1: "))
                b = float(input("Enter no.2: "))

                if operation == "+":
                    result = self.calculator.add(a,b)

                elif operation == "-":
                    result = self.calculator.sub(a,b)

                elif operation == "*":
                      result = self.calculator.mul(a,b)

                elif operation == "/":
                    result = self.calculator.div(a,b)

                elif operation == "%":
                    result = self.calculator.percent(a,b)

                else:
                    return ("Vaue error: Try again")

                print(f"Result: {result}")
                print ('_' * 30)
                continue
            
            except ValueError:
                print ("Value error! Enter vaild no.")
                continue


if __name__ == "__main__":
    app = calculator()
    app.menu()
    app.operation()
