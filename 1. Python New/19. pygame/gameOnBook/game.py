import pygame
import sys
import random
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Get the base directory of the script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load assets using absolute paths
BACKGROUND_IMG = pygame.image.load(os.path.join(BASE_DIR, "../module 3/bg.png"))
CHARACTER_IMG = pygame.image.load(os.path.join(BASE_DIR, "../module 3/f1.png"))
OBSTACLE_IMG = pygame.image.load(os.path.join(BASE_DIR, "../module 3/bg2.png"))

# Scale assets
BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG, (WIDTH, HEIGHT))
CHARACTER_IMG = pygame.transform.scale(CHARACTER_IMG, (50, 50))
OBSTACLE_IMG = pygame.transform.scale(OBSTACLE_IMG, (50, 200))

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Book Theme Flappy Bird")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Character position
character_x = 100
character_y = HEIGHT // 2
character_velocity = 0

# Gravity
gravity = 0.3  # Reduced gravity for slower falling
jump_strength = -12  # Increased jump strength for higher jumps

# Obstacles
obstacles = []
obstacle_speed = 3  # Slower obstacle movement
obstacle_frequency = 2000  # Increased time between obstacles
last_obstacle_time = pygame.time.get_ticks()

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.blit(BACKGROUND_IMG, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                character_velocity = jump_strength

    # Update character position
    character_velocity += gravity
    character_y += character_velocity

    # Prevent character from going off-screen
    if character_y < 0:
        character_y = 0
    elif character_y > HEIGHT - CHARACTER_IMG.get_height():
        character_y = HEIGHT - CHARACTER_IMG.get_height()
        character_velocity = 0  # Stop falling when hitting the ground

    # Draw character
    screen.blit(CHARACTER_IMG, (character_x, character_y))

    # Generate obstacles
    current_time = pygame.time.get_ticks()
    if current_time - last_obstacle_time > obstacle_frequency:
        obstacle_x = WIDTH
        gap_y = random.randint(150, HEIGHT - 350)  # Larger gap for easier passage
        obstacles.append((obstacle_x, gap_y))
        last_obstacle_time = current_time

    # Move and draw obstacles
    for i, obstacle in enumerate(obstacles[:]):
        obstacle_x, gap_y = obstacle
        obstacle_x -= obstacle_speed

        # Update the obstacle position in the list
        obstacles[i] = (obstacle_x, gap_y)

        # Remove obstacles that go off-screen
        if obstacle_x < -OBSTACLE_IMG.get_width():
            obstacles.pop(i)
            score += 1

        # Draw upper and lower obstacles
        screen.blit(OBSTACLE_IMG, (obstacle_x, gap_y - OBSTACLE_IMG.get_height()))  # Upper obstacle
        screen.blit(OBSTACLE_IMG, (obstacle_x, gap_y + 150))  # Lower obstacle

        # Check for collision
        if (character_x < obstacle_x + OBSTACLE_IMG.get_width() and
            character_x + CHARACTER_IMG.get_width() > obstacle_x and
            (character_y < gap_y or character_y > gap_y + 150)):
            running = False

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

pygame.quit()
sys.exit()