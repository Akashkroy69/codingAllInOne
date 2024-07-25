# Define a Car class
class Car:
    # Class attribute (shared by all cars)
    number_of_wheels = 4

    # Initialize the object with attributes
    def __init__(self, make, model, year, color):
        # Instance attributes
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False

    # Instance method (behavior)
    def start_engine(self):
        self.is_running = True
        print(f"The {self.color} {self.make} {self.model}'s engine is running.")

# Create car objects
car1 = Car("Toyota", "Camry", 2022, "blue")
car2 = Car("Honda", "Civic", 2023, "red")

# Access object attributes
print(car1.make)  # Output: Toyota
print(car2.color)  # Output: red

# Call object methods
car1.start_engine()  # Output: The blue Toyota Camry's engine is running.
car2.start_engine()  # Output: The red Honda Civic's engine is running.



# from pygame import mixer

# import time

# # Starting the mixer

# mixer.init()

# # Loading the song

# mixer.music.load("kbc-awesome-5410.mp3")

# # Setting the volume

# mixer.music.set_volume(0.7)

# # Start playing the song

# mixer.music.play()

# # infinite loop

# while True:

# print("Press 'p' to pause, 'r' to resume")

# print("Press 'e' to exit the program")

# query = input(" ")

# if query == 'p':

# # Pausing the music

# mixer.music.pause()

# elif query == 'r':

# # Resuming the music

# mixer.music.unpause()

# elif query == 'e':

# # Stop the mixer

# mixer.music.stop()

# break

# name = input("What is your name? \n")

# print("==========================")

# print("==========================")

# print(f"WELCOME TO KBC MR {name}!")

# print("So, Let's begin the game")

# print("==========================")

# print("\n The first ques on your screen for 1000 points\n\n What is the largest planet in the universe?\n\n A.Earth\nB.Jupiter\nC.J1407B\nD.Sagitarious - A\n\n Give Your Answer Quickly\n")

# ans1 = input("Enter your answer: ")

# if ans1 == "C":

# print("Correct Answer, congratulations! You won 1000 points")

# print(f"A huge round of applause for MR {name}")

# mixer.init()

# # Loading the song

# mixer.music.load("JV4BSDN-claps.mp3")

# # Setting the volume

# mixer.music.set_volume(0.7)

# # Start playing the song

# mixer.music.play()

# # infinite loop

# while True:

# print("Press 'p' to pause, 'r' to resume")

# print("Press 'e' to exit the program")

# query = input(" ")

# if query == 'p':

# # Pausing the music

# mixer.music.pause()

# elif query == 'r':

# # Resuming the music

# mixer.music.unpause()

# elif query == 'e':

# # Stop the mixer

# mixer.music.stop()

# break

# elif ans1 == "c":

# print("Correct Answer, congratulations! You won 1000 points")

# print(f"A huge round of applause for MR {name}")

# time.sleep(1)

# mixer.init()

# # Loading the song

# mixer.music.load("JV4BSDN-claps.mp3")

# # Setting the volume

# mixer.music.set_volume(0.7)

# # Start playing the song

# mixer.music.play()

# # infinite loop

# while True:

# print("Press 'p' to pause, 'r' to resume")

# print("Press 'e' to exit the program")

# query = input(" ")

# if query == 'p':

# # Pausing the music

# mixer.music.pause()

# elif query == 'r':

# # Resuming the music

# mixer.music.unpause()

# elif query == 'e':

# # Stop the mixer

# mixer.music.stop()

# break

# else:

# print("Wrong Answer, you lost")

# exit()