import turtle
import random

# Set up the game window
window = turtle.Screen()
window.title("Pen🖊️ - Gun🔫 - Scissors✂️ Game")
window.bgcolor("lightblue")
window.setup(width=600, height=400)
window.tracer(0)

# Define weapons and their corresponding emojis
weapon_list = {"pen": "🖊️", "scissors": "✂️", "gun": "🔫"}

# Create the player's weapon turtle
player_weapon = turtle.Turtle()
player_weapon.hideturtle()

# Function to display the player's weapon
def show_player_weapon(weapon):
    player_weapon.clear()
    player_weapon.write(weapon_list[weapon], align="center", font=("Arial", 48, "normal"))

# Get the user's choice and convert it to lowercase for consistency
user_choice = window.textinput("Pen🖊️ - Gun🔫 - Scissors✂️ Game", "Enter your choice (pen, scissors, or gun): ").lower()

# Check if the user's choice is valid (pen, scissors, or gun)
if user_choice in weapon_list:
    # Computer randomly selects its choice (pen, scissors, or gun)
    computer_choice = random.choice(["pen", "scissors", "gun"])
    
    # Set up the computer's weapon turtle
    computer_weapon = turtle.Turtle()
    computer_weapon.penup()
    computer_weapon.hideturtle()
    computer_weapon.goto(200, 0)
    computer_weapon.write(weapon_list[computer_choice], align="center", font=("Arial", 48, "normal"))
    
    # Determine the winner based on the user's and computer's choices
    if weapon_list[user_choice] == weapon_list[computer_choice]:
        result = "It's a tie!"
    elif weapon_list[user_choice] == "🖊️" and weapon_list[computer_choice] == "✂️":
        result = "Computer wins!"
    elif weapon_list[user_choice] == "✂️" and weapon_list[computer_choice] == "🔫":
        result = "Computer wins!"
    elif weapon_list[user_choice] == "🔫" and weapon_list[computer_choice] == "🖊️":
        result = "Computer wins!"
    else:
        result = "You win!"
    
    # Display the result
    result_turtle = turtle.Turtle()
    result_turtle.penup()
    result_turtle.hideturtle()
    result_turtle.goto(0, -150)
    result_turtle.write(result, align="center", font=("Arial", 24, "bold"))
else: 
    print("Invalid choice. Please choose pen, scissors, or gun.")

# Keep the window open until manually closed by the user
turtle.done()
