# Method to calculate numbers
def calculate_number(num1, num2, operation):
    if operation.__eq__('+'):
        return num1 + num2
    elif operation.__eq__('-'):
        return num1 - num2
    elif operation.__eq__('*'):
        return num1 * num2
    elif operation.__eq__('/'):
        if num2 == 0: return "Dividend cannot be zero!"
        return num1 / num2
    else:
        return "Invalid operator!"

if __name__ == '__main__':

    input("This is a basic calculator. Press Enter to continue...")
    number_1 = int(input("Enter 1st number: "))
    number_2 = int(input("Enter 2nd number: "))
    operator = input("Enter operator (+, -, *, /): ")

    result = calculate_number(number_1, number_2, operator)

    if type(result) is int or type(result) is float:
        print(f"Result of {number_1} {operator} {number_2} is {result}")
    else:
        print("Oops! Something went wrong,Please try again.")
        print(f"Reason: {result}")