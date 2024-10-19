import pygame
from pygame import *

# Initialize Pygame
pygame.init()

# Set up the screen
screen = display.set_mode((700, 500))
background = transform.scale(image.load("galaxy.jpg"), (700, 500))

# Base class for sprites
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

# Player class
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 65:  # Adjusting for sprite width
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 65:  # Adjusting for sprite height
            self.rect.y += self.speed

# Enemy class (currently empty)
class Enemy(GameSprite):
    def update(self):
        pass  # Add enemy movement logic here

# Game setup
game = True
clock = time.Clock()
FPS = 60

# Create player and enemy instances
player = Player("rocket.png", 100, 100, 5)  # Replace with your image path
enemy = Enemy("asteroid.png", 300, 100, 5)  # Replace with your image path

# Create sprite groups
monsters = sprite.Group()
monsters.add(enemy)

# Load and play music
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play(-1)  # Loop the music

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    # Update
    player.update()
    monsters.update()

    # Draw everything
    screen.blit(background, (0, 0))
    player.reset()
    monsters.draw(screen)

    # Update display
   
    display.update()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()

