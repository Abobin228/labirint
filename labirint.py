import pygame



pygame.init()
screen = pygame.display.set_mode((300, 300))
while True:
    screen.fill('grey')
    pygame.draw.line(screen, 'white', (100, 0 ), (100, 300), 5)
    pygame.draw.line(screen, 'white', (200, 0 ), (200, 300), 5)
    pygame.draw.line(screen, 'white', (0, 100 ), (300, 100), 5)
    pygame.draw.line(screen, 'white', (0, 200 ), (300, 200), 5)
    pygame.draw.line(screen, 'red', (0, 100 ), (100, 100), 5)
    pygame.draw.line(screen, 'red', (100, 200 ), (200, 200), 5)
    pygame.draw.line(screen, 'red', (0, 100 ), (100, 100), 5)
    pygame.draw.line(screen, 'red', (0, 0 ), (0, 300), 5)
    pygame.draw.line(screen, 'red', (0, 0 ), (300, 0), 5)
    pygame.draw.line(screen, 'red', (300, 0 ), (300, 300), 5)
    pygame.draw.line(screen, 'red', (0, 300 ), (300, 300), 5)
    pygame.display.flip()





