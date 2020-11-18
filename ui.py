import pygame
import random
import time
from logic import *
from variables import *
from images import *

# Variables 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hunger Games!")
clock = pygame.time.Clock()
mobs = pygame.sprite.Group()
enemies = pygame.sprite.Group()
foods = pygame.sprite.Group()
damage = 1600


# Загрузка всей игровой графики
background = pygame.image.load(path.join(img_dir, 'background.png')).convert()
player_img = pygame.image.load(path.join(img_dir, "che.jpg")).convert()
enemy_img = pygame.image.load(path.join(img_dir, "mic.jpg")).convert()
font = pygame.font.Font(pygame.font.get_default_font(), 36)

# Add food to the screen
for i in range(random.randint(2000, 4000)):
    m = Food()
    foods.add(m)

    

# Add cells to the screen
for i in range(50):
    m = EnemyMob(enemy_img)
    enemies.add(m)



# Add cells to the screen
for i in range(50):
    m = Mob(player_img)
    mobs.add(m)


# The Main Loop
running = True
while running:
	# Rendering food
    m = Food()
    foods.add(m)

    clock.tick(FPS)

    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            running = False

    # If a cell eats, it becomes stronger
    for mob in mobs:
        for food in foods:
            if mob.rect.colliderect(food.rect):
                mob.strength += food.calories


    for mob2 in enemies:
        for food in foods:
            if mob2.rect.colliderect(food.rect):
                mob2.strength += food.calories
                

    if len(mobs) <= 10 or len(enemies) <= 10:
    	damage = 500 
   

    # Checking for collisions
    for mob in mobs:
    	for mob2 in enemies:
    		# The stronger mob wins, the weaker dies
    		if mob.rect.colliderect(mob2.rect):
    			if mob.strength > mob2.strength:
    				mob2.strength -= mob.strength / damage

    				if mob2.strength <= 0:
    					mob.strength += mob2.strength
    					enemies.remove(mob2)

    			if mob2.strength > mob.strength:
    				mob.strength -= mob2.strength / damage

    				if mob.strength <= 0:
    					mob2.strength += mob.strength
    					mobs.remove(mob)

    			else:
    				pass


    # Food disapears, if hit
    hits = pygame.sprite.groupcollide(mobs, foods, False, True)
    hits = pygame.sprite.groupcollide(enemies, foods, False, True)
    enemies.update()
    mobs.update()
    foods.update()


    # Fillig the screen with black color
    background_rect = background.get_rect()
    screen.blit(background, background_rect)

    mobs.draw(screen)
    foods.draw(screen)
    enemies.draw(screen)

    # Adding all entyties to the screenc
    pygame.display.flip()

pygame.quit()