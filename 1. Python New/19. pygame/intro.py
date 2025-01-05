import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Intro")

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)  

img = pygame.image.load(r"19. pygame\vayun.png")
img = pygame.transform.scale(img, (50, 150))

posCircleX = width // 2
posCircleY = height // 2

posVayunY = height // 2 + 50
posVayunX = width // 2 - 50

runningState = True
while runningState:

    screen.fill(WHITE)
    screen.blit(img, (posVayunX, posVayunY))
    posVayunX += 0.1

    pygame.draw.circle(screen, RED, (posCircleX,posCircleY), 50)
    pygame.display.update()

    posCircleY+= 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit event detected")
            runningState = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                posCircleY -= 100
                posVayunX += 10
            elif event.key == pygame.K_DOWN:
                posCircleY += 10
            elif event.key == pygame.K_RIGHT:
                posCircleX += 10
            elif event.key == pygame.K_LEFT:
                posCircleX -= 10
    # pygame.display.flip()

    
pygame.quit()
sys.exit()