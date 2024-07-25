# You can also use a finally block to execute code that 
# should run regardless of whether an exception occurred or not. For example:
try:
    # Code that might cause an error
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Invalid input, please enter a number")
finally:
    print("Execution completed.")

# The finally block is useful for tasks like closing files or cleaning up resources.