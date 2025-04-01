#OOP CONCEPTS ON CALCULATOR
# Object-Oriented Programming (OOP) concepts in Python


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
