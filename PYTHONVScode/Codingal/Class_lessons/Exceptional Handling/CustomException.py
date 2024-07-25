# Custom Exceptions:

# You can create your own custom exceptions to handle specific errors in your code. For example:

class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed")
    print("You entered:", num)
except NegativeNumberError as e:
    print("Error:", e)
# Here, we've defined a custom NegativeNumberError and raised it when a negative number is entered.