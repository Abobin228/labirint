import pygame
import random


pygame.init()
screen = pygame.display.set_mode((300, 300))
a = 50
b = 50

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
pygame.draw.rect(screen, 'green',(205, 205, 92, 92))
pygame.draw.circle(screen, 'blue', (a, b ),(20))
running = True
while running:
    # Держим цикл на правильной скорости
# Ввод процесса (события)
    for event in pygame.event.get():
# check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if a == 250 and b == 250:
              pygame.draw.rect(screen, 'green',(0, 0, 300, 300))
              
                  
            elif a == 50 and b == 50 and event.key == pygame.K_DOWN:
              a = a
              b = b
            elif a == 150 and b == 150 and event.key == pygame.K_DOWN:
              a = a
              b = b
            elif a == 50 and b == 150 and event.key == pygame.K_UP:
              a = a
              b = b
            elif a == 150 and b == 250 and event.key == pygame.K_UP:
              a = a
              b = b
            elif event.key == pygame.K_DOWN:
              if b + 100 > 300:
                pygame.draw.circle(screen, 'blue', (a,b), 20)
              else:
                pygame.draw.circle(screen, 'blue', (a,b + 100 ), 20) 
                pygame.draw.circle(screen, 'grey', (a,b ), 20)
                b+=100
                if a == 250 and b == 250:
                  pygame.draw.rect(screen, 'green',(0, 0, 300, 300))
                  pygame.draw.line(screen, 'yellow', (50, 100 ), (75, 200),15)
                  pygame.draw.line(screen, 'yellow', (75, 200 ), (100, 150),15)
                  pygame.draw.line(screen, 'yellow', (100, 150 ), (125, 200),15)
                  pygame.draw.line(screen, 'yellow', (125, 200 ), (150, 100),15)
                  pygame.draw.line(screen, 'yellow', (175, 100 ), (175, 200),15)
                  pygame.draw.line(screen, 'yellow', (200, 100 ), (200, 200),15)
                  pygame.draw.line(screen, 'yellow', (200, 100 ), (275, 200),15)
                  pygame.draw.line(screen, 'yellow', (275, 100 ), (275, 200),15)
            elif event.key == pygame.K_UP:
              if b - 100 < 0:
                pygame.draw.circle(screen, 'blue', (a,b), 20)
              else:
                pygame.draw.circle(screen, 'blue', (a,b - 100 ), 20) 
                pygame.draw.circle(screen, 'grey', (a,b ), 20)
                b-=100
                if a == 250 and b == 250:
                  pygame.draw.rect(screen, 'green',(0, 0, 300, 300))
            elif event.key == pygame.K_RIGHT:
              if a + 100 > 300:
                pygame.draw.circle(screen, 'blue', (a,b), 20)
              else:
                pygame.draw.circle(screen, 'blue', (a+100,b ), 20) 
                pygame.draw.circle(screen, 'grey', (a,b ), 20)
                a+=100
                if a == 250 and b == 250:
                  pygame.draw.rect(screen, 'green',(0, 0, 300, 300))
            elif event.key == pygame.K_LEFT:
              if a - 100 < 0:
                pygame.draw.circle(screen, 'blue', (a,b), 20)
              else:
                pygame.draw.circle(screen, 'blue', (a - 100,b), 20) 
                pygame.draw.circle(screen, 'grey', (a,b ), 20)
                a-=100
                if a == 250 and b == 250:
                  pygame.draw.rect(screen, 'green',(0, 0, 300, 300))
    pygame.display.flip()



