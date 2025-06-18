import traceback

try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Oops! You can't divide by zero.")
    else:
        print(f"Division successful. Result = {result}")
    finally:
        print("Division operation attempted.")


divide(10, 2)
divide(10, 0)


# Runtime Error
try:
    mobile_number = int(input("Enter mobile number: "))
except ValueError:
    print("Invalid input! Please enter a valid integer for age.")


try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Oops! File not found.")


try:
    num = int(input("Enter a number: "))
    print(100 / num)
except ValueError:
    print("Not a number!")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print(f"Unexpected error: {e}")


def withdraw(amount):
    if amount <= 0:
        raise ValueError("Amount must be positive integer!")
    return f"Withdrew ₹{amount}"


try:
    print(withdraw(int(input("Enter amount to withdraw: "))))
except ValueError as e:
    print(f"Error: {e}")


try:
    age = int(input("Enter your age: "))
    assert age >= 0, "Age can't be negative!"
except ValueError as e:
    print(traceback.format_exc())
    print(f"Value Error: {e}")
except AssertionError as e:
    print(traceback.format_exc())
    print(f"Assertion Error: {e}")
