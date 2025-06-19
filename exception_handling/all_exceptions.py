# I/O Exceptions
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Insufficient permissions to access the file.")
except IOError as e:
    print(f"I/O Error occurred: {e}")

# System Exceptions
try:
    result = 10 / 0  # Causes a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero.")

# Runtime Exceptions
try:
    int_value = int("abc")  # Causes a ValueError
except ValueError as e:
    print(f"Value Error: {e}")

try:
    my_list = [1, 2, 3]
    print(my_list[10])  # Causes an IndexError
except IndexError as e:
    print(f"Index Error: {e}")


# User-Defined Exceptions
class InvalidInputError(Exception):
    pass


def validate_input(value):
    if value < 0:
        raise InvalidInputError("Error: Input must be non-negative.")
    return value**2


try:
    result = validate_input(-5)
except InvalidInputError as e:
    print(e)

# Handling Multiple Exceptions
try:
    result = 10 / 0
    int_value = int("abc")
except (ZeroDivisionError, ValueError) as e:
    print(f"Multiple Exceptions Caught: {e}")

# Using `else` and `finally` Blocks
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero.")
else:
    print(f"Result: {result}")
finally:
    print("This block will always execute.")


def some_function():
    try:
        # Code that might raise an exception
        pass
    except Exception as e:
        print(f"An error occurred: {e}")


# Catching the General Exception
try:
    some_function()
except Exception as e:
    print(f"An error occurred: {e}")
