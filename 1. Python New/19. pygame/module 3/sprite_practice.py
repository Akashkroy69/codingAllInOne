import pygame

pygame.init()
# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Sprite Practice")

class Player(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.image = pygame.image.load(r"19. pygame\vayun.png")  # Load the image
        self.image = pygame.transform.scale(self.image, (50, 150))
        self.rect = self.image.get_rect()
        self.rect.topleft = (posX, posY)

    def update(self):
        self.rect.x += 0.1

class Circle(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)  # Create a surface with transparency
        pygame.draw.circle(self.image, "red", (50, 50), 50)  # Draw a red circle on the surface
        self.rect = self.image.get_rect()
        self.rect.center = (posX, posY)
    
    def update(self):
        self.rect.y += 0.1

circle = Circle(width // 2, height // 2)
player = Player(width // 2 - 50, height // 2 + 50)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(circle)

runningState = True

while runningState:
    screen.fill("white")  # Fill the screen with white
    all_sprites.update()  # Update all sprites
    all_sprites.draw(screen)  # Draw all sprites on the screen


    player.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit event detected")
            runningState = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.rect.y -= 10
            elif event.key == pygame.K_DOWN:
                player.rect.y += 10
            elif event.key == pygame.K_RIGHT:
                player.rect.x += 10
            elif event.key == pygame.K_LEFT:
                player.rect.x -= 10
        if event.type == pygame.MOUSEMOTION:
            circle.rect.topleft = event.pos
    if pygame.sprite.collide_rect(player, circle):
        # __delete player
        print("Collision detected between player and circle!")
       
    pygame.display.update()
