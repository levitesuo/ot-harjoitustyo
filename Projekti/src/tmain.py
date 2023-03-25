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

    if platforms.check_for_collisions(meitti._floor_box):
        # print(meitti._floor_box)
        meitti.on_the_floor()
        if keys[pygame.K_UP]:
            meitti.apply_force((0, -100))
    meitti.update()
    platforms.draw(screen)

    if keys[pygame.K_LEFT]:
        meitti.apply_force((-5, 0))
    if keys[pygame.K_RIGHT]:
        meitti.apply_force((5, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    c.tick(30)
    pygame.display.update()
