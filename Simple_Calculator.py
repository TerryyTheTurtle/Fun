# This is the banner section
whose_calculator = "Welcome to Terry The Turtle's simple calculator"
pretty_banner = "=" * len(whose_calculator)

print(f"{pretty_banner}\n{whose_calculator}\n{pretty_banner}\n") # Printers the banner in 3 rows

# Define calculations
def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    if num2 == 0:
        return None
    return num1 / num2

while True:
    # Prompt for the first number
    while True:
        first_number = input("Please enter the first number (decimal is allowed): ")
        try:
            first_number = float(first_number)
            break
        except ValueError:
            print("ERROR: That is not a numerical value. Please try again\n")

    # Prompt for the second number
    while True:
        second_number = input("Please enter the second number (decimal is allowed): ")
        try:
            second_number = float(second_number)
            break
        except ValueError:
            print("ERROR: That is not a numerical value. Please try again\n")

    # Prompt for the parameter for the 2 number input's
    while True:
        print("\n1: Add, 2: Subtract, 3: Multiply, 4: Divide")
        parameter_select = input("Please enter a number from 1-4 for the parameter: ")

        try:
            parameter_select = int(parameter_select)
            if parameter_select in range(1,5):
                total = None
                if parameter_select == 1:
                    print(f"\nInput: {first_number} + {second_number}")
                    total = add(first_number, second_number)
                elif parameter_select == 2:
                    print(f"\nInput: {first_number} - {second_number}")
                    total = subtract(first_number, second_number)
                elif parameter_select == 3:
                    print(f"\nInput: {first_number} * {second_number}")
                    total = multiply(first_number, second_number)
                elif parameter_select == 4:
                    print(f"\nInput: {first_number} / {second_number}")
                    total = divide(first_number, second_number)
                break
            else:
                print("ERROR: That is an invalid selection. Please enter a number between 1-4")
        except ValueError:
            print("ERROR: That is an invalid selection. Please enter a number between 1-4")

    # Print the answer
    if total is None:
        print("ERROR: Cannot divide by 0")
    else:
        print(f"Answer: {total:.2f}")

    # Prompt if the user would like to continue
    encore = input("\nWould you like to continue? (y/N): ")
    if encore.lower() == "y" or encore.lower() == "yes":
        print(pretty_banner)
        continue
    else:
        print("\nThank you for using the calculator! Please come again!")
        break
