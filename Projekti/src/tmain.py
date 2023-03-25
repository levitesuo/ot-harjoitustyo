from game_files.level_entities.level_platforms import LevelPlatforms as LP
from game_files.entities.player import Player
import pygame

platform0 = ((0, 300), 400)
platform1 = ((100, 100), 100)
platform2 = ((100, 200), 50)
platform3 = ((50, 250), 75)
platforms = LP([platform0, platform1, platform2, platform3])

meitti = Player((200, 200))

pygame.init()
c = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))

screen.fill((150, 150, 150))
pygame.display.flip()

while True:
    screen.fill((150, 150, 150))
    screen.blit(meitti.sprite, (meitti._pos[0], meitti._pos[1]))
    keys = pygame.key.get_pressed()
    meitti.apply_force((0, 10))
    player_new_pos = meitti.calc_new_pos()
    collision = platforms.check_for_collisions(meitti.falling_box(player_new_pos))
    print(collision)
    if collision:
        print("C")
        if keys[pygame.K_UP]:
            meitti.apply_force((0, -10))
        if keys[pygame.K_LEFT]:
            meitti.apply_force((-5, 0))
        if keys[pygame.K_RIGHT]:
            meitti.apply_force((5, 0))
        new_pos = (player_new_pos[0], collision)
        meitti.floor_hit(new_pos)
    else:
        meitti.apply_force((0 ,10))
        meitti.falling(player_new_pos)
        
    platforms.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    c.tick(10)
    pygame.display.update()
