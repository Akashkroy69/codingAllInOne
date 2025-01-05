import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("First Game")

RED = (250, 2, 2) #
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# infinite loop
runningState = True
while runningState:
      screen.fill(RED)
      pygame.display.update()
  # we have to write the game and UI logic that will basically keep drawing the visual components
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  runningState = False


pygame.quit()

# pip install pygame