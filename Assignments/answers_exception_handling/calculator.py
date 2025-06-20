def addition(num1, num2):
    print(f"Addition is {num1 + num2}")

def subtraction(num1, num2):
    print(f"Subtraction is {num1 - num2}")

def division(num1, num2):
    try:
        print(f"Division is {num1 / num2}")
    except ZeroDivisionError:
        print("Second number cannot be zero")

def multiplication(num1, num2):
    print(f"Multiplication is {num1 * num2}")

def square_root(num1):
    try:
        assert num1 <= 0, "Number cannot be negative"
        print(f"Square root is {num1 ** 0.5}")
    except AssertionError as msg:
        print(msg)


while True:
    print("[1] perform addition\n[2] perform subtraction\n[3] Perform division\n[4] Perform multiplication\n[5] Perform square root operation\n[6] Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 5:
            num1 = int(input("Enter a number: "))
        elif choice != 6:
            num1 = int(input("Enter 1st no.:"))
            num2 = int(input("Enter 2nd no.:"))
    except ValueError:
        print("Please enter valid number as a input")
        continue

    # NOTE: you need python version 3.10 or higher to use "match". If not, use if-else ladder
    match choice:
        case 1:
            addition(num1, num2)
        case 2:
            subtraction(num1, num2)
        case 3:
            division(num1, num2)
        case 4:
            multiplication(num1, num2)
        case 5:
            square_root(num1)
        case 6:
            print("Exiting the application...")
            break
        case _:
            print("Enter a valid number shown above")
        

