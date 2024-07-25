# Exception handling in Python is a way to deal 
# with errors or unexpected situations in your code. 
# It helps your program continue running smoothly even when something goes wrong.

try:
    # Code that might cause an error
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    # This block runs if a ZeroDivisionError occurs
    print("Error: Cannot divide by zero")
except ValueError:
    # This block runs if a ValueError occurs (e.g., when input is not a number)
    print("Error: Invalid input, please enter a number")
except Exception as e:
    # This block handles other exceptions
    print("An error occurred:", e)

    # We try to perform some calculations inside the try block.
    # If an error (exception) occurs, we jump to the corresponding except block. 
    # In this example, we handle ZeroDivisionError, ValueError, and a generic Exception.
print("=======================")

# example: student document verification: let us say that you with your friends are  standing. If you forgot to bring any of the doc,
# the person starts screaming and stops verifying for other students too... you wudn't want that, right? He should mange this well
