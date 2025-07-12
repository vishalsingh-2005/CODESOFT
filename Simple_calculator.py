def get_user_input():
    try:
        num1 = float(input("\nEnter first number: "))
        operator = input("Enter operator (+, -, *, /, %, **): ")
        num2 = float(input("Enter second number: "))
        return num1, operator, num2
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return None, None, None

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return None
    elif operator == '%':
        return num1 % num2
    elif operator == '**':
        return num1 ** num2
    else:
        print("Invalid operator! Please use +, -, *, /, % or **.")
        return None

def main():
    print("\n---Welcome to the Simple Calculator!---")
    while True:
        num1, operator, num2 = get_user_input()
        if num1 is None or operator is None or num2 is None:
            continue
        result = calculate(num1, operator, num2)
        if result is not None:
            print(f"The result of {num1} {operator} {num2} = {result}")
        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("\nThank you for using the calculator! Goodbye!\n")
            break

if __name__ == "__main__":
    main()  
