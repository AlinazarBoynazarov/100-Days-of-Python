from logging import root
import math

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def square_root(n1):
    return math.sqrt(n1)

def power(n1, n2):
    return math.pow(n1, n2)


operations = {

"+": add, 
"-": subtract,
"*": multiply,
"/": divide,


}

def calculator():
    from art import logo    
    print(logo)
    should_continue = True

    num1 = float(input("Please insert a first number: "))
    for key in operations:
        print(key)

    while should_continue:
        symbol = input("Please select an operator from the choice above: ")
        num2 = float(input("Plese select the second number: "))
        function = operations[symbol]
        answer = function(num1, num2)

        print(f"{num1} {symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
            
    
        
    

