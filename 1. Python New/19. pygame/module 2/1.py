import pygame


pygame.init()


# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Intro")
clock = pygame.time.Clock()
runningState = True

font = pygame.font.Font(None, 36)  # Create a font object

text = font.render("Move the mouse!", True, "black")  # Render the text


posX = width
posY = height

while runningState:
    screen.fill("red")  # Fill the screen with white
    pygame.draw.circle(screen, "white", (width // 2, height // 2), 50)  # Draw a white circle at the center
    pygame.draw.rect(screen, "green", (posX // 2 - 50, posY // 2 + 50, 100, 50))  # Draw a green rectangle below the circle
    pygame.draw.line(screen, "blue", (0, 0), (posX, posY), 15)  # Draw a blue diagonal line
    pygame.draw.line(screen, "green", (10, 10), (posX+30, posY+30), 15)  # Draw a blue diagonal line
    pygame.draw.line(screen, "yellow", (20, 30), (posX+50, posY+50), 15)  # Draw a blue diagonal line

    screen.blit(text, (10, 10))  # Draw the text on the screen

    posX -= 1  # Move the rectangle to the left
    # posY -= 0.1  # Move the circle up
    if posX < 0:  # Reset position if it goes off screen
        posX = width

    pygame.display.update()  # Update the display
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit event detected")
            runningState = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                posY -= 10
        elif event.type == pygame.MOUSEMOTION:
            posX, posY = event.pos
            print(f"Mouse moved to: {posX}, {posY}")
    clock.tick(200)  # Limit the frame rate to 60 FPS


pygame.quit()  # Quit Pygame