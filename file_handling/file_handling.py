import io
import os
import shutil

try:
    file = open("example.txt", "r")  # Opens file in read mode
except FileNotFoundError:
    print("File not found. Please check the file path.")
finally:
    if "file" in locals():
        file.close()


try:
    file = open("example.txt", "w")  # Opens file in write mode
    file.write("Hello, World!")  # Writes to the file
    file.close()  # Closes the file after writing
except IOError:
    print("An error occurred while writing to the file.")

# Reading from a file (input stream)
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# File is closed automatically here

# Writing to a file (output stream)
with open("example.txt", "w") as file:
    file.write("New content")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

with open("example.txt", "a") as file:
    file.write("\tAppended content")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)


try:
    # with open("example_multiline.txt", "w") as file:
    with open("example_multiline.txt", "w+") as file:
        file.write("Line 1\nLine 2\n")
        file.write("Line 3\n")

        lines = ["Line 4", "Line 5"]
        file.writelines(lines)

        # file.seek(0)
        content = file.read()
        print(f"file content is as: \n{content}")
        print("----------- end of file ------------")
except io.UnsupportedOperation:
    print("Operation does not support")

with open("example_multiline.txt", "r") as file:
    content = file.read()
    print(content)

    file.seek(0)  # Move the file pointer to the beginning
    lines = file.readlines()
    for line in lines:
        print(line.strip())
        # print(f"line {lines.index(line) + 1}:", line.strip())


with open("example_byte.txt", "wb") as file:
    file.write(
        b"123456789 Hello, World! This is a byte string. You can write bytes here."
    )

with open("example_byte.txt", "r") as file:
    print(file.tell())  # Current position (bytes)
    file.seek(10)  # Move to 10th byte
    print(file.read(5))  # Read next 5 bytes
    print(file.tell())  # Current position (bytes)
    file.seek(0)  # Move to the beginning
    print(file.tell())  # Current position (bytes)


stats = os.stat("example.txt")
print(f"Size: {stats.st_size} bytes")
print(f"Last modified: {stats.st_mtime}")
print(f"Last accessed: {stats.st_atime}")
print(f"Last changed: {stats.st_ctime}")


print(os.path.exists("example.txt"))
print(os.path.exists("example123.txt"))

print(os.path.isfile("example.txt"))
print(os.path.isfile("directory"))

print(os.path.isdir("example.txt"))
print(os.path.isdir("directory"))


os.rename("old.txt", "new.txt")  # Rename
os.remove("file.txt")  # Delete file
shutil.copy("source.txt", "dest.txt")  # Copy
os.mkdir("new_dir")  # Create directory
print(os.listdir())  # List files in current directory
path = "."
print(os.listdir(path))  # List files in provided path
size_in_bytes = os.path.getsize("./example.txt")
print(size_in_bytes)
