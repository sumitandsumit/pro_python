# String Basics
greeting = "Hello, World!"
multiline_string = """This is a
multiline
string."""
print(greeting)
print(multiline_string)

# String Indexing and Slicing
name = "John Doe"
print(name[0])  # Output: J
print(name[5:8])  # Output: Doe
print(name[-3:])  # Output: Doe
print(name[::-1])  # Output: eoD nhoJ


# String Concatenation and Repetition
greeting = "Hello " + "there!"
print(greeting)  # Output: Hello there!
print("Python" * 3)  # Output: PythonPythonPython

# String Formatting
name = "Alice"
print(f"Hello, {name}!")  # Output: Hello, Alice!
print("Hello, {}!".format(name))  # Output: Hello, Alice!

# String Methods
text = "   hello   "
print(text.strip())  # Output: hello
print("python".upper())  # Output: PYTHON
print("Hello, World!".split(", "))  # Output: ['Hello', 'World!']

# Unicode and Encodings
french_greeting = "Bonjour, le monde!"
greek_letters = "\u03b1\u03b2\u03b3"
print(french_greeting)
print(greek_letters)

# Real-Life Examples
# User Input
name = input("What is your name? ")
print(f"Hello, {name}!")

# File Paths
file_path = "documents/report.txt"

# URL Handling
url = "https://www.example.com/index.html"
domain = url.split("/")[2]
print(domain)  # Output: www.example.com

# Text Processing
text = "The quick brown fox jumps over the lazy dog."
word_count = text.count("the")
print(word_count)  # Output: 2

# Data Formatting
from datetime import datetime

date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(date_str)
