import pygame
pygame.init()
pygame.mixer.init()                           # make sure mixer is ready

hit_sound = pygame.mixer.Sound(r"C:\Users\Lenovo\OneDrive\Desktop\aaVS_CODE\1. Python New\19. pygame\module 5 audio\myst.mp3.mp3")     # put a .wav or .ogg in the same folder
hit_sound.set_volume(0.7)                     # 0.0-1.0  (optional)

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()


class Bat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((120, 20))
        self.image.fill("blue")
        self.rect = self.image.get_rect(midbottom=(300, 560))

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "red", (15, 15), 15)
        self.rect = self.image.get_rect(center=(x, y))
        self.vy = 4                               # falls down each frame

    def update(self):
        self.rect.y += self.vy

bat   = Bat()
ball  = Ball(300, 50)

player_group = pygame.sprite.Group(bat)
ball_group   = pygame.sprite.Group(ball)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # simple left / right control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]  and bat.rect.left  > 0:   bat.rect.x -= 6
    if keys[pygame.K_RIGHT] and bat.rect.right < 600: bat.rect.x += 6

    # update & draw
    ball_group.update()

    screen.fill("white")
    player_group.draw(screen)
    ball_group.draw(screen)

    # ▶️  collision check – play sound once for each hit
    hits = pygame.sprite.spritecollide(bat, ball_group, False)   # False → keep ball
    if hits:                                                    
        hit_sound.play(maxtime=1000)          # play the sound effect
        ball.vy *= -1             # simple bounce so you hear repeated hits

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
