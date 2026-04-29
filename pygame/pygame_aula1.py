import pygame
import random

pygame.init()
tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption('EPIC 67 Game')

fundo = (0, 0, 0)
running = True

x = 250
y = 250
vel = 0.5
r = 0
b = 0
g = 250

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_SPACE]:
        r = random.randint(0, 250)
        b = random.randint(0, 250)
        g = random.randint(0, 250)

    if x >= 640 - 67:
        x = 640 - 67
    if y >= 480 - 67:
        y = 480 - 67

    if x <= 67:
        x = 67
    if y <= 67:
        y = 67
    tela.fill(fundo)
    pygame.draw.circle(tela, (r, g, b), (x, y), 67)
    pygame.display.flip()

pygame.quit()