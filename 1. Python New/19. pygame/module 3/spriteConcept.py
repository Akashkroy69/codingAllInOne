import pygame 
import random

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Sprite Concept")
backgraound = pygame.image.load(r"19. pygame\module 3\bg7.png")
# Scale the background image to fit the screen
backgraound = pygame.transform.scale(backgraound, (width, height))

gameOverText = pygame.font.Font(None, 74).render("Game Over", True, "red")
# score 
scoreFont = pygame.font.Font(None, 36)

# lives text
livesFont = pygame.font.Font(None, 36)

players = [
     r"19. pygame\module 3\1_.png",
     r"19. pygame\module 3\2_.png",
    r"19. pygame\module 3\3_.png",
    r"19. pygame\module 3\4_.png",
]

players = [pygame.image.load(player) for player in players]
players = [pygame.transform.scale(player, (50, 160)) for player in players]  # Scale the images to desired size



class Player(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        # self.image = pygame.Surface((150, 50), pygame.SRCALPHA)  # Create a surface with transparency
        # self.image.fill("blue")
        self.frames = players  # Use the list of player images
        self.current_frame = 0  # Start with the first frame
        self.image = self.frames[self.current_frame]  # Set the initial image
        self.rect = self.image.get_rect()
        self.rect.center = (posX, posY)
        self.animationTimer = 0  # Timer to control animation speed
        self.animation_speed = 10  # Speed of animation

    def update(self):
        self.animationTimer += 1
        if self.animationTimer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]  # Update the image to the next frame
            self.animationTimer = 0  # Reset the timer
    def flip(self):
         for i in range(len(self.frames)):
            self.frames[i] = pygame.transform.flip(self.frames[i], True, False)
class Circle(pygame.sprite.Sprite):
    def __init__(self, posX, posY,color):
        super().__init__()
        # self.image = pygame.Surface((100, 100), pygame.SRCALPHA)  # Create a surface with transparency
        # pygame.draw.circle(self.image, color, (50, 50), 20)  # Draw a red circle on the surface
        self.imageOriginal = pygame.image.load(random.choice(list_of_bombs))
        self.imageOriginal = pygame.transform.scale(self.imageOriginal, (100, 100))  # Scale the image to desired size
        self.image = self.imageOriginal.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (posX, posY)
        self.angle = 0  # Initialize angle for rotation

    def update(self):
        self.rect.y += 1  # Move the circle downwards
        self.angle = (self.angle+1)%360 # Increment the angle for rotation
        self.image = pygame.transform.rotate(self.imageOriginal, self.angle)  # Rotate the image slightly for effect
        self.rect = self.image.get_rect(center=self.rect.center)  # Update the rect to match the new image position
    

# bomb color list
bomb_colors = ["red", "green", "yellow", "purple", "orange"]
list_of_bombs = [
     r"19. pygame\module 3\f1.png",
     r"19. pygame\module 3\f2.png",
     r"19. pygame\module 3\f3.png",
     r"19. pygame\module 3\f4.png",
     r"19. pygame\module 3\f5.png",
     r"19. pygame\module 3\f6.png",
     r"19. pygame\module 3\f7.png",
     r"19. pygame\module 3\f8.png"
]

player = Player(width // 2 - 50, height - 65)
circle = Circle(width // 2, 30, random.choice(bomb_colors))  # Create a circle at the top with a random color
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
bomb = pygame.sprite.Group()
bomb.add(circle)
clock = pygame.time.Clock()  # Create a clock to control the frame rate
runningState = True
count = 0
score = 0

ballMissed = 0
toRight = True
while runningState:
    screen.fill("white")  # Fill the screen with white
    screen.blit(backgraound, (0, 0))  # Draw the background image
    all_sprites.draw(screen)  # Draw all sprites on the screen
    bomb.draw(screen)  # Draw the circle
    score_text = scoreFont.render(f"Score: {score}", True, "black")  # Render the score text
    screen.blit(score_text, (10, 10))  # Draw the score text on the screen
    # lives
    lives_text = livesFont.render(f"Lives Missed: {ballMissed}", True, "black")  # Render the lives text
    screen.blit(lives_text, (10, 40))  # Draw the lives text on the screen
    count += 1
    if count % 100 == 0:  # Every 100 frames, add a new circle
        new_circle = Circle(random.randint(0,width),random.randint(0, 10), random.choice(bomb_colors))  # Create a new circle at a random position with a random color
        bomb.add(new_circle)
    
    if ballMissed >= 5:
                # print("Game Over! Too many balls missed.")
                player.kill()  # Remove the player sprite if a bomb goes off screen
                bomb.empty()
                screen.blit(gameOverText, (width // 2 - 150, height // 2 - 50))
    else:
         bomb.update()  # Update the circles
         all_sprites.update()  # Update all sprites

         
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit event detected")
            runningState = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and player.rect.x < width - player.rect.width:
                player.rect.x += 30
                if toRight== False:
                    player.flip()
                    toRight = True
            elif event.key == pygame.K_LEFT and player.rect.x > 0:
                player.rect.x -= 30
                if toRight == True:
                    player.flip()
                    toRight = False
            elif event.key == pygame.K_SPACE:
                 if toRight:
                    player.rect.x += 80
                 else:
                    player.rect.x -= 80
            # u char key press : jumping feature --> pending
            # elif event.key == pygame.K_u:
            #     count = 0
            #     while count < 100:
            #         player.rect.y -= 1
            #         count += 1
    
    if pygame.sprite.spritecollideany(player, bomb):
         bomb_hit = pygame.sprite.spritecollide(player, bomb, True)
         if bomb_hit: score += len(bomb_hit)
         for hit in bomb_hit:
                print(f"Hit a bomb of color: {hit.image.get_at((50, 50))}")
    for anyBomb in bomb:
        if anyBomb.rect.top > height:
            anyBomb.kill()
            ballMissed += 1
            print(f"Ball missed! Total missed: {ballMissed}")
          
           
                
    clock.tick(60)  # Limit the frame rate to 60 FPS
    pygame.display.update()  # Update the display
pygame.quit()  # Quit Pygame