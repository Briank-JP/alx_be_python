# prompt the user to input the two numbers and store them in two variables
num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

# prompt the user to choose an operation 
operation = input("Choose the operation (+, -, *, /): ")

# perform the chosen operation and store the result in a variable
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num2 - num1
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
            print("Cannot divide by zero.")