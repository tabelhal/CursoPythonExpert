import pygame, math, os, random

pygame.init()
W, H = 800, 600
win = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)
pygame.display.set_caption('Asteriords Game')

HIGHSCORE_FILE = 'highscore.txt'
if os.path.exists(HIGHSCORE_FILE):
    with open(HIGHSCORE_FILE, 'r') as f:
        highscore = int(f.read())
else:
    highscore = 0

player_pos = [W//2, H//2]
player_speed = 5
player_lives = 3

fundo = (0, 0, 0)
running = True

x = 250
y = 250
vel = 0.10
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


    if x >= 640 - 15:
        x = 640 - 15
    if y >= 480 - 15:
        y = 480 - 15

    if x <= 15:
        x = 15
    if y <= 15:
        y = 15
    pygame.draw.circle((r, g, b), (x, y), 15)
    pygame.display.flip()

pygame.quit()