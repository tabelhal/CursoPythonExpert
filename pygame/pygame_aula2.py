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

bullets = []
last_shot = 0
shot_cooldown = 300

asteroids = []

asteroid_types =[
    {'size': 20, 'speed':3, 'points':15, 'color':(200, 200, 255)},
    {'size': 30, 'speed': 2, 'points': 10, 'color': (180, 180, 180)},
    {'size': 50, 'speed': 1.5, 'points': 5, 'color': (150, 150, 150)}
]

powerups = []
powerup_active = False
powerup_timer = 0

STATE_MENU = 0
STATE_GAME = 1
STATE_GAMEOVER = 2
game_state = STATE_MENU

def spawn_asteriod():
    t = random.choice(asteroid_types)
    x = random.randint(0, W)
    y = random.choice([-50, H+50])
    angle = math.atan2(H//2 - y, W//2 - x)
    asteroids.append([x, y, t['speed'], angle, t['points'], t['color']])

def spawn_powerup():
    x = random.randint(50, W-50)
    y = random.randint(50, H-50)
    powerups.append([x, y, 'shield'])

def reset_game():
    global player_pos, player_lives, score, asteroids, bullets, powerups
    player_pos = [W//2, H//2]
    player_lives = 3
    score = 0
    asteroids = []
    bullets = []
    powerups = []
    for _ in range(6):
        spawn_asteriod()

running = True
spawn_timer = 0
spawn_interval = 3000
last_powerup = 0
powerup_interval = 10000

while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_state == STATE_MENU and event.type == pygame.K_RETURN:
                reset_game()
                game_state = STATE_GAME
            elif game_state == STATE_GAMEOVER and event.key == pygame.K_RETURN:
                reset_game()
                game_state = STATE_GAME

keys = pygame.key.get_pressed()
if game_state == STATE_GAME:
    if keys[pygame.K_w] or keys[pygame.K_UP]: player_pos[1] -= player_speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]: player_pos[1] += player_speed
    if keys[pygame.K_a] or keys[pygame.K_LEFT]: player_pos[0] -= player_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]: player_pos[0] += player_speed

    if keys[pygame.K_SPACE] and pygame.time.get_ticks() - last_shot > shot_cooldown:
        last_shot = pygame.time.get_ticks()
        bullets.append([player_pos[0], player_pos[1], 0, -0])

    for b in bullets:
        b[1] += b[3]
    bullets = [b for b in bullets if 0 < b[1] < H]

    for a in asteroids:
        a[0] += math.cos(a[4]) * a[2]
        a[1] += math.cos(a[4]) * a[2]

    spawn_timer += dt
    if spawn_timer > spawn_interval:
        spawn_asteriod()
        spawn_timer = 0
        if spawn_interval > 1000:
            spawn_interval -= 50

    if pygame.time.get_ticks() - last_powerup > powerup_interval:
        spawn_powerup()
        last_powerup = pygame.time.get_ticks()

    if powerup_active and pygame.time.get_ticks() > powerup_timer:
        powerup_active = False

    new_asteroids = []
    for a in asteroids:
        ax, ay, sp, sz, ang, pts, color = a
        hit = False
        for b in bullets:
            

pygame.quit()