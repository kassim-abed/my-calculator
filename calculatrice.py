import os

# Forbidden symbols 
forbidden_symbols = "=£$!§&%µ@#?^<>.:[{}]~()"

# Forbidden letters
forbidden_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

while True:
    number1 = float(input("Enter the first number (integer or decimal) : "))
    operation = input("Enter the desired operation (+, -, *, /): ")
    
    # check if the characters are written
    if any(char in forbidden_symbols for char in operation):
        print(f"Error: The symbol '{operation}' is not allowed in the operation. Please enter a valid operation.")
        
    # check if the characters are written
    elif any(char in forbidden_letters for char in operation):
        print(f"Error: The letter '{operation}' is not allowed in the operation. Please enter a valid operation.")

    else:
        number2 = float(input("Enter the second number (integer or decimal): "))

        if operation == "+":
            result = number1 + number2
        elif operation == "*":
            result = number1 * number2
        elif operation == "-":
            result = number1 - number2
        elif operation == "/":
            try:            
                result = number1 / number2
                #peut etre essayer de faire une function pour la division , avec le try/except a l'interieur(division)
            except ZeroDivisionError :
                print('salut')    
                print(f"the result of {number1} {operation} {number2} is: {result}")
                break

