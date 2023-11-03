def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):

    if num2 != 0:
        return num1 / num2
    else:
        return " Error: Cannot divide by zero"

#Greeting the user

print("Welcome to the simple calculator!")

operation = input("Choose the operation (+, -, *, /):")

first_number = float(input("Enter the first number: "))

second_number = float(input("Enter the second number: "))

if operation == '+':
    print("The sum of", first_number, "and" , second_number, "is:", add_numbers(first_number, second_number))
elif operation == "-":
    print("The Difference of", first_number, "and", second_number, "is:", subtract_numbers(first_number, second_number))
elif operation == "*":
    print("The product of", first_number, "and", second_number, "is", multiply_numbers(first_number, second_number))
elif operation == "/":
    print("The quotient of", first_number, "and", second_number, "is", divide_numbers(first_number, second_number))
else:
    print("invalid operation. Please slect from +, -, *, or /.")
