import pygame
import random
from pygame import mixer

pygame.init()  # initialize pygame

screen = pygame.display.set_mode((800, 600))

# Title
pygame.display.set_caption("Space Invasion")

# Icon - download from flaticon
icon = pygame.image.load("worldwide.png")
pygame.display.set_icon(icon)

# Background
bg = pygame.image.load("14237502_5438849.jpg")

# mixer music
mixer.music.load("Cargo Plane Cabin Ambiance-SoundBible.com-589803489.mp3")
mixer.music.set_volume(0.7)         # sets the volume from 0 to 1
mixer.music.play(-1)        # -1 plays sound on loop


# player variables
player = pygame.image.load("space-invaders-2.png")

# aligning the player
x = 368  # subtract the pixels from total height and divide by 2
y = 500  # subtract the pixels from total width and divide by 2
speed = 0

# enemy variables
enemy = []
x2 = []
y2 = []
speed2 = []
height = []
num = 6

for e in range(num):
    enemy.append(pygame.image.load("alien.png"))
    x2.append(random.randint(0, 736))
    y2.append(random.randint(50, 200))
    speed2.append(0.5)
    height.append(50)

# bullet variables
bullet = pygame.image.load("bullet.png")
x3 = 0
y3 = 500
height2 = 3
visible = False

# score var
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textx = 10
testy = 10

# end of game
endf = pygame.font.Font("freesansbold.ttf", 50)


def scoreshown(x,y):
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (x, y))


def final():
    final_font = endf.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(final_font, (250, 250))

def playeronscreen(x, y):
    screen.blit(player, (x, y))


def enemyonscreen(x, y, enem):
    screen.blit(enemy[enem], (x, y))


def shoot(x, y):
    global visible
    visible = True
    screen.blit(bullet, (x + 16, y + 10))


def collision(a, b, c, d):
    dist = (((a - b) ** 2) + ((c - d) ** 2)) ** 0.5
    if dist < 27:
        return True
    else:
        return False


playing = True
# game loop
while playing:
    # rgb background
    screen.blit(bg, (0, 0))

    # Handling events
    for event in pygame.event.get():

        # closing event
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = -0.9
            if event.key == pygame.K_RIGHT:
                speed = 0.9
            if event.key == pygame.K_SPACE:
                bullets = mixer.Sound("Missle_Launch-Kibblesbob-2118796725.mp3")
                bullets.play()
                bullets.set_volume(0.5)
                if not visible:
                    x3 = x
                    shoot(x3, y3)
        # release key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed = 0
            if event.key == pygame.K_SPACE:
                bullets = mixer.Sound("Missle_Launch-Kibblesbob-2118796725.mp3")
                bullets.play()
                bullets.set_volume(0.5)
                if not visible:
                    x3 = x
                    shoot(x3, y3)
    # modify player location
    x += speed

    # keep player inside screen
    if x <= 0:
        x = 0
    elif x >= 736:
        x = 736

    # modify enemy location
    for en in range(num):
        # end of game
        if y2[en] > 500:
            for k in range(num):
                y2[k] = 1000
            final()
            break
        x2[en] += speed2[en]


        # keep enemy inside screen
        if x2[en] <= 0:
            speed2[en] = 1
            y2[en] += height[en]

        elif x2[en] >= 736:
            speed2[en] = -1
            y2[en] += height[en]

        # collision
        coll = collision(x2[en], y2[en], x3, y3)
        if coll:
            colls = mixer.Sound("Shotgun_Blast-Jim_Rogers-1914772763.mp3")
            colls.play()
            colls.set_volume(0.3)
            y3 = 500
            visible = False
            score += 1
            x2[en] = random.randint(0, 736)
            y2[en] = random.randint(50, 200)
        enemyonscreen(x2[en], y2[en], en)

    # bullets movement
    if y3 <= 32:
        y3 = 500
        visible = False
    if visible:
        shoot(x3, y3)
        y3 -= height2

    # print player and enemy on screen
    playeronscreen(x, y)
    scoreshown(textx, testy)
    # update
    pygame.display.update()
