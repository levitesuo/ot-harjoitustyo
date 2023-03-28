import pygame
import sys
from game_files.entities.player import Player
from game_files.level_entities.level_platforms import LevelPlatforms

pygame.init()
sizex = 1000
sizey = 800
clock = pygame.time.Clock()

screen = pygame.display.set_mode((sizex, sizey))

pl1 = ((0, sizey - 10), sizex)
pl2 = ((sizex / 3, 730), sizex / 3)
platforms = LevelPlatforms([pl1, pl2])

meitti = Player((sizex / 2, sizey / 2))

while True:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        meitti.apply_force((0, -10))
    if keys[pygame.K_DOWN]:
        meitti.apply_force((0, 10))
    if keys[pygame.K_LEFT]:
        meitti.apply_force((-10, 0))
    if keys[pygame.K_RIGHT]:
        meitti.apply_force((10, 0))

    player_boxes = meitti.get_falling_bounding_boxes()
    for box in player_boxes:
        collision = platforms.check_for_collisions(box)
        meitti.collision_handler(collision)

    screen.fill((100, 100, 100))
    platforms.draw(screen)
    screen.blit(meitti.sprite, meitti._pos)
    meitti.update()
    events = pygame.event.get()
    pygame.display.flip()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
    clock.tick(30)
