if __name__ == "__main__":
    import pygame
    import level_objects as lo
    import sys
    
    pygame.init()
    
    xsize = 800
    ysize = 800
    
    screen = pygame.display.set_mode((xsize, ysize))
    clock = pygame.time.Clock()
    player = lo.player((200, 200))
    movement = [0, 0]
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: movement[1] -= 1
                elif event.key == pygame.K_DOWN: movement[1] += 1
                elif event.key == pygame.K_RIGHT: movement[0] += 1
                elif event.key == pygame.K_LEFT: movement[0] -= 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP: movement[1] = 0
                elif event.key == pygame.K_DOWN: movement[1] = 0
                elif event.key == pygame.K_RIGHT: movement[0] = 0
                elif event.key == pygame.K_LEFT: movement[0] = 0
        
        player.move((movement[0], movement[1]))
        player.updateAndShow()
        screen.fill(0)
        screen.blit(player._sprite, (player._pos[0], player._pos[1]))
        pygame.display.update()
        clock.tick(60)