import pygame
import random


pygame.init()
screen = pygame.display.set_mode((300, 300))

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
running = True
while running:
    # Держим цикл на правильной скорости
# Ввод процесса (события)
    for event in pygame.event.get():
# check for closing window
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()




