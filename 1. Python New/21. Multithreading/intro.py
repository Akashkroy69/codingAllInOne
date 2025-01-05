import threading


def print_numbers():
    for i in range(1, 100):
        print(i, end=' ')

def print_letters():
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        print(letter, end=' ')

# print_numbers()
# print_letters()

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()



print("done")