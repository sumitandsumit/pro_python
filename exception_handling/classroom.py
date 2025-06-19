try:
    variable = int(input("Please enter a number: "))
except ValueError as e:
    print("Please enter a valid number")
else:
    result = variable + 100
    print(result)
finally:
    print("code executed")
