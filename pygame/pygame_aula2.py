import pygame, math, os, random

pygame.init()

W, H = 800, 600
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mini Asteroids")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

HIGHSCORE_FILE = "highscore.txt"

if os.path.exists(HIGHSCORE_FILE):
    with open(HIGHSCORE_FILE, "r") as f:
        highscore = int(f.read())
else:
    highscore = 0

STATE_MENU = 0
STATE_GAME = 1
STATE_GAMEOVER = 2

game_state = STATE_MENU

player_pos = [W // 2, H // 2]
player_speed = 5
player_lives = 3

bullets = []
asteroids = []

score = 0

last_shot = 0
shot_cooldown = 300

asteroid_types = [
    {"size": 20, "speed": 3, "points": 15, "color": (200, 200, 255)},
    {"size": 30, "speed": 2, "points": 10, "color": (180, 180, 180)},
    {"size": 50, "speed": 1.5, "points": 5, "color": (150, 150, 150)},
]


def spawn_asteroid():
    t = random.choice(asteroid_types)

    x = random.randint(0, W)
    y = random.choice([-50, H + 50])

    angle = math.atan2(player_pos[1] - y, player_pos[0] - x)

    asteroids.append([
        x,
        y,
        t["speed"],
        angle,
        t["size"],
        t["points"],
        t["color"]
    ])


def reset_game():
    global player_pos, player_lives, bullets, asteroids, score

    player_pos = [W // 2, H // 2]
    player_lives = 3
    bullets = []
    asteroids = []
    score = 0

    for _ in range(5):
        spawn_asteroid()


running = True

spawn_timer = 0
spawn_interval = 2000

while running:

    dt = clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if game_state == STATE_MENU and event.key == pygame.K_RETURN:
                reset_game()
                game_state = STATE_GAME

            elif game_state == STATE_GAMEOVER and event.key == pygame.K_RETURN:
                reset_game()
                game_state = STATE_GAME

    keys = pygame.key.get_pressed()

    if game_state == STATE_GAME:

        if keys[pygame.K_w]:
            player_pos[1] -= player_speed

        if keys[pygame.K_s]:
            player_pos[1] += player_speed

        if keys[pygame.K_a]:
            player_pos[0] -= player_speed

        if keys[pygame.K_d]:
            player_pos[0] += player_speed

        if keys[pygame.K_SPACE]:

            if pygame.time.get_ticks() - last_shot > shot_cooldown:

                last_shot = pygame.time.get_ticks()

                bullets.append([
                    player_pos[0],
                    player_pos[1],
                    0,
                    -10
                ])

        for b in bullets:
            b[1] += b[3]

        bullets = [b for b in bullets if 0 < b[1] < H]

        for a in asteroids:

            a[0] += math.cos(a[3]) * a[2]
            a[1] += math.sin(a[3]) * a[2]

        spawn_timer += dt

        if spawn_timer > spawn_interval:
            spawn_asteroid()
            spawn_timer = 0

        new_asteroids = []

        for a in asteroids:

            ax, ay, sp, ang, sz, pts, color = a

            hit = False

            for b in bullets:

                if math.hypot(ax - b[0], ay - b[1]) < sz:

                    bullets.remove(b)
                    hit = True
                    score += pts
                    break

            if not hit:
                new_asteroids.append(a)

        asteroids = new_asteroids

        for a in asteroids:

            if math.hypot(a[0] - player_pos[0], a[1] - player_pos[1]) < a[4] + 20:

                player_lives -= 1

                if player_lives <= 0:

                    game_state = STATE_GAMEOVER

                    if score > highscore:

                        highscore = score

                        with open(HIGHSCORE_FILE, "w") as f:
                            f.write(str(highscore))

    win.fill((0, 0, 20))

    if game_state == STATE_MENU:

        title = font.render("MINI ASTEROIDS", True, (255, 255, 255))
        txt = font.render("ENTER para começar", True, (200, 200, 200))

        win.blit(title, (W // 2 - 120, H // 2 - 40))
        win.blit(txt, (W // 2 - 120, H // 2 + 10))

    elif game_state == STATE_GAME:

        pygame.draw.circle(win, (0, 255, 0), player_pos, 20)

        for b in bullets:
            pygame.draw.circle(win, (255, 255, 0), (int(b[0]), int(b[1])), 5)

        for a in asteroids:
            pygame.draw.circle(
                win,
                a[6],
                (int(a[0]), int(a[1])),
                a[4]
            )

        hud = font.render(
            f"Score: {score}   Vidas: {player_lives}",
            True,
            (255, 255, 255)
        )

        win.blit(hud, (10, 10))

    elif game_state == STATE_GAMEOVER:

        over = font.render("GAME OVER", True, (255, 0, 0))
        txt = font.render("ENTER para reiniciar", True, (255, 255, 255))

        win.blit(over, (W // 2 - 100, H // 2 - 40))
        win.blit(txt, (W // 2 - 140, H // 2 + 10))

    pygame.display.flip()

pygame.quit()