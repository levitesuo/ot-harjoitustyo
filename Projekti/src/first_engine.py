if __name__ == "__main__":
    import pygame
    import level_objects as lo
    import sys
    
    pygame.init()
    
    xsize = 800
    ysize = 800
    
    screen = pygame.display.set_mode((xsize, ysize))
    
    player = lo.player((200, 200))
    
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: player.move((0, -1))
                elif event.key == pygame.K_DOWN: player.move((0, 1))
                elif event.key == pygame.K_RIGHT: player.move((1, 0))
                elif event.key == pygame.K_LEFT: player.move((-1, 0))
        player.updateAndShow()
        screen.fill(0)
        screen.blit(player._sprite, (player._pos[0], player._pos[1]))
        pygame.display.update()