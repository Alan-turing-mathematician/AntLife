import pygame
import random
import time
from variables import *

# Class for food
class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.calories = random.choice([100, 40, 70, 30])
        self.image = pygame.Surface((2, 2))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH)
        self.rect.y = random.randrange(HEIGHT)


# Class for cells  
class Mob(pygame.sprite.Sprite, object):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.strength = random.randrange(10)
        self.size = random.choice([random.randrange(10, 100), random.randrange(20, 60), random.randrange(20, 60)])
        self.image = pygame.transform.scale(img, (self.size, self.size))
        self.image.set_colorkey((238,238,238))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange((WIDTH - self.size) // 2, WIDTH - self.size)
        self.rect.y = random.randrange(0, (HEIGHT - self.size) // 2)
        self.speedy = random.randrange(1, round(1/self.size * 200)) * random.choice([-1, 1])
        self.speedx = random.randrange(1, round(1/self.size * 200)) * random.choice([-1, 1])

    def update(self):
        
        # Not allowing cells to go beyond the boundaries by x
        if self.rect.x >= WIDTH or self.rect.x <= 0:
            if self.speedx != -1 or self.speedx != 1:
                self.speedx += random.choice([-1, 0, 0, 1])

            self.speedx *= -1

            
        
        # Not allowing cells to go beyond the boundaries by y
        if self.rect.y >= HEIGHT or self.rect.y <= 0:
            if self.speedy != -1 or self.speedy != 1:
                self.speedy += random.choice([-1, 0, 0, 1]) 

            self.speedy *= -1

        # moving the ball 
        self.rect.y += self.speedy
        self.rect.x += self.speedx 



# Class for cells  
class EnemyMob(pygame.sprite.Sprite, object):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.strength = random.randrange(10)
        self.size = random.choice([random.randrange(10, 100), random.randrange(20, 60), random.randrange(20, 60)])
        self.image = pygame.transform.scale(img, (self.size, self.size))
        self.image.set_colorkey((248,248,248))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, (WIDTH - self.size) // 2)
        self.rect.y = random.randrange(0, (HEIGHT - self.size) // 2)
        self.speedy = random.randrange(1, round(1/self.size * 200)) * random.choice([-1, 1])
        self.speedx = random.randrange(1, round(1/self.size * 200)) * random.choice([-1, 1])

    def update(self):
        
        # Not allowing cells to go beyond the boundaries by x
        if self.rect.x >= WIDTH or self.rect.x <= 0:         
            self.speedx *= -1 
        
        # Not allowing cells to go beyond the boundaries by y
        if self.rect.y >= HEIGHT or self.rect.y <= 0:            
            self.speedy *= -1

        # moving the ball 
        self.rect.y += self.speedy
        self.rect.x += self.speedx
       