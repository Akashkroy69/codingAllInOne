import pygame

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Load music
pygame.mixer.music.load(r"C:\Users\Lenovo\OneDrive\Desktop\aaVS_CODE\1. Python New\19. pygame\module 5 audio\myst.mp3.mp3")
pygame.mixer.music.play(-1)  # Loop indefinitely

# Set up screen
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Music in Pygame")

running = True
while running:
    screen.fill("lightblue")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
