with open("example_byte.bin", "wb+") as file:
    binary_string = (
        b"123456789 Hello, World! This is a byte string. You can write bytes here."
    )
    print(len(binary_string))
    file.write(binary_string)

    print(file.tell())  # Current position (bytes)
    file.seek(0)  # Move to the beginning
    print(file.tell())  # Current position (bytes)
    file.seek(10)  # Move to 10th byte
    print(file.read(5))  # Read next 5 bytes
    print(file.tell())  # Current position (bytes)
    file.seek(0)  # Move to the beginning
    print(file.tell())  # Current position (bytes)
