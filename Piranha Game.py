#!/usr/bin/env python
import pygame

# COLORS    R    G    B
white = (255, 255, 255)
black = (0,   0,   0)

# IMAGES
wallH_image = pygame.image.load('wallH.png')
wallH = pygame.transform.scale(wallH_image, (140, 32))
wallH2_image = pygame.image.load('wallH2.png')
wallH2 = pygame.transform.scale(wallH2_image, (800, 32))
wallV = pygame.image.load('wallV1.png')
wallV2 = pygame.image.load('wallV2.png')
wallV3 = pygame.image.load('wallV3.png')
player1up_image = pygame.image.load('player1up.png')
player1spriteup = pygame.transform.scale(player1up_image, (28, 28))
player1down_image = pygame.image.load('player1down.png')
player1spritedown = pygame.transform.scale(player1down_image, (28, 28))
player1right_image = pygame.image.load('player1right.png')
player1spriteright = pygame.transform.scale(player1right_image, (28, 28))
player1left_image = pygame.image.load('player1left.png')
player1spriteleft = pygame.transform.scale(player1left_image, (28, 28))
player2up_image = pygame.image.load('player2up.png')
player2spriteup = pygame.transform.scale(player2up_image, (28, 28))
player2down_image = pygame.image.load('player2down.png')
player2spritedown = pygame.transform.scale(player2down_image, (28, 28))
player2right_image = pygame.image.load('player2right.png')
player2spriteright = pygame.transform.scale(player2right_image, (28, 28))
player2left_image = pygame.image.load('player2left.png')
player2spriteleft = pygame.transform.scale(player2left_image, (28, 28))

# GAME CLASSES


class Player(pygame.sprite.Sprite):
    def __init__(self, player_number):
        pygame.sprite.Sprite.__init__(self)
        if player_number == 1:
            self.image = player1sprite
        if player_number == 2:
            self.image = player2sprite
        self.rect = self.image.get_rect()

    def update(self, direction, player_direction):
        if player_direction == 'left' or player_direction == 'right':
            self.rect.x += direction

        elif player_direction == 'up' or player_direction == 'down':
            self.rect.y += direction


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(white)
        self.rect = self.image.get_rect()

    def update(self, shoot_direction, bullet_number):
        if bullet_number == 1:
            if shoot_direction == 'down':
                self.rect.y += 10
            elif shoot_direction == 'right':
                self.rect.x += 10
            elif shoot_direction == 'up':
                self.rect.y -= 10
            elif shoot_direction == 'left':
                self.rect.x -= 10
        if bullet_number == 2:
            if shoot_direction == 'down':
                self.rect.y += 10
            elif shoot_direction == 'right':
                self.rect.x += 10
            elif shoot_direction == 'up':
                self.rect.y -= 10
            elif shoot_direction == 'left':
                self.rect.x -= 10


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, orientation):
        pygame.sprite.Sprite.__init__(self)
        if orientation == 'horizontal':
            self.image = wallH
        elif orientation == 'horizontal2':
            self.image = wallH2
        elif orientation == 'vertical':
            self.image = wallV
        elif orientation == 'vertical2':
            self.image = wallV2
        elif orientation == 'vertical3':
            self.image = wallV3
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

# GAME FUNCTIONS


def create_wall(wall_type):
    wall = Wall(wallX[wall_number], wallY[wall_number], wall_type)
    sprites_list.add(wall)
    walls_list.add(wall)


def player_turn(player_direction, player_number, player1, player2, sprites1, sprites2):
    if player_number == 1:
        sprites = sprites1
        player_prevX = player1.rect.x
        player_prevY = player1.rect.y
        player_list = player1_list
        sprites_list.remove(player1)
        player_list.remove(player1)
    elif player_number == 2:
        sprites = sprites2
        player_prevX = player2.rect.x
        player_prevY = player2.rect.y
        player_list = player2_list
        sprites_list.remove(player2)
        player_list.remove(player2)
    if player_direction == 'down':
        playersprite = sprites[0]
    elif player_direction == 'up':
        playersprite = sprites[1]
    elif player_direction == 'right':
        playersprite = sprites[2]
    elif player_direction == 'left':
        playersprite = sprites[3]
    player = Player(player_number)
    sprites_list.add(player)
    player_list.add(player)
    return player, playersprite, player_prevX, player_prevY, player_list


# PYGAME INITIATION
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Piranha Game')

# FONT
fontpath = "Arwing.ttf"
myfont = pygame.font.Font(fontpath, 75)

# ENTITY GROUPS
sprites_list = pygame.sprite.Group()
bullet1_list = pygame.sprite.Group()
bullet2_list = pygame.sprite.Group()
player1_list = pygame.sprite.Group()
player2_list = pygame.sprite.Group()
walls_list = pygame.sprite.Group()

# CREATES PLAYER 1
player1sprite = player1spriteup
player1 = Player(1)
sprites_list.add(player1)
player1_list.add(player1)
player1.rect.x = 387
player1.rect.y = 525
player1_hp = 5

# CREATES PLAYER 2
player2sprite = player2spritedown
player2 = Player(2)
sprites_list.add(player2)
player2_list.add(player2)
player2.rect.x = 387
player2.rect.y = 50
player2_hp = 5

# CREATES WALLS
wallX = [100, 560, 100, 560, 100, 100, 560, 560, 155,
         155, 615, 615, 385, 385, 300, 470,  0,   0, 768,   0]
wallY = [470, 470, 100, 100, 330, 235, 330, 235, 330,
         175, 330, 175, 100, 400, 150, 150,  0, 569,   0,   0]
wall_number = 0

for wall in range(20):
    if wall_number < 8:
        wall_type = 'horizontal'
        create_wall(wall_type)
    elif 8 <= wall_number < 14:
        wall_type = 'vertical'
        create_wall(wall_type)
    elif 14 <= wall_number < 16:
        wall_type = 'vertical2'
        create_wall(wall_type)
    elif 16 <= wall_number < 18:
        wall_type = 'horizontal2'
        create_wall(wall_type)
    elif 18 <= wall_number < 20:
        wall_type = 'vertical3'
        create_wall(wall_type)
    wall_number += 1

# OTHER VARIABLES
done = False
clock = pygame.time.Clock()
player_speed = 3.5
winner = 0
player_direction = 'up'
player_direction2 = 'down'
bullet1_count = 0
bullet2_count = 0
shoot_direction = 'up'
shoot_direction2 = 'down'
sprites1 = [player1spritedown, player1spriteup,
            player1spriteright, player1spriteleft]
sprites2 = [player2spritedown, player2spriteup,
            player2spriteright, player2spriteleft]

# MAIN GAME LOOP
while done == False:
    pygame.event.pump()
    keys = pygame.key.get_pressed()

    # PLAYER 1 CONTROLS
    if keys[pygame.K_s]:
        player_direction = 'down'

        player1.update(player_speed, player_direction)
        player1, player1sprite, player1.rect.x, player1.rect.y, player1_list = player_turn(
            player_direction, 1, player1, player2, sprites1, sprites2)

    if keys[pygame.K_w]:
        player_direction = 'up'
        player1.update(-player_speed, player_direction)
        player1, player1sprite, player1.rect.x, player1.rect.y, player1_list = player_turn(
            player_direction, 1, player1, player2, sprites1, sprites2)

    if keys[pygame.K_d]:
        player_direction = 'right'
        player1.update(player_speed, player_direction)
        player1, player1sprite, player1.rect.x, player1.rect.y, player1_list = player_turn(
            player_direction, 1, player1, player2, sprites1, sprites2)

    if keys[pygame.K_a]:
        player_direction = 'left'
        player1.update(-player_speed, player_direction)
        player1, player1sprite, player1.rect.x, player1.rect.y, player1_list = player_turn(
            player_direction, 1, player1, player2, sprites1, sprites2)

    # PLAYER 2 CONTROLS
    if keys[pygame.K_DOWN]:
        player_direction2 = 'down'
        player2.update(player_speed, player_direction2)
        player2, player2sprite, player2.rect.x, player2.rect.y, player2_list = player_turn(
            player_direction2, 2, player1, player2, sprites1, sprites2)

    if keys[pygame.K_UP]:
        player_direction2 = 'up'
        player2.update(-player_speed, player_direction2)
        player2, player2sprite, player2.rect.x, player2.rect.y, player2_list = player_turn(
            player_direction2, 2, player1, player2, sprites1, sprites2)

    if keys[pygame.K_RIGHT]:
        player_direction2 = 'right'
        player2.update(player_speed, player_direction2)
        player2, player2sprite, player2.rect.x, player2.rect.y, player2_list = player_turn(
            player_direction2, 2, player1, player2, sprites1, sprites2)

    if keys[pygame.K_LEFT]:
        player_direction2 = 'left'
        player2.update(-player_speed, player_direction2)
        player2, player2sprite, player2.rect.x, player2.rect.y, player2_list = player_turn(
            player_direction2, 2, player1, player2, sprites1, sprites2)

    # SHOOTS BULLET
    for event in pygame.event.get(pygame.KEYDOWN):
        if event.key == pygame.K_SPACE and bullet1_count == 0:
            bullet1 = Bullet()
            bullet1.rect.x = player1.rect.x + 7
            bullet1.rect.y = player1.rect.y + 7
            sprites_list.add(bullet1)
            bullet1_list.add(bullet1)
            bullet1_count = 1
            shoot_direction = player_direction

        if event.key == pygame.K_RCTRL and bullet2_count == 0:
            bullet2 = Bullet()
            bullet2.rect.x = player2.rect.x + 7
            bullet2.rect.y = player2.rect.y + 7
            sprites_list.add(bullet2)
            bullet2_list.add(bullet2)
            bullet2_count = 1
            shoot_direction2 = player_direction2

    bullet1_list.update(shoot_direction, 1)
    bullet2_list.update(shoot_direction2, 2)

    # CHECKS IF BULLET HITS OR MISSES
    for bullet1 in bullet1_list:
        player2_hit = pygame.sprite.spritecollide(bullet1, player2_list, False)
        bullet1_hits_wall = pygame.sprite.spritecollide(
            bullet1, walls_list, False)

        for player2 in player2_hit:
            bullet1_list.remove(bullet1)
            sprites_list.remove(bullet1)
            player2_hp -= 1
            bullet1_count = 0
            if player2_hp == 0:
                sprites_list.empty()
                winner = 1

        for wall in bullet1_hits_wall:
            walls_list.remove(bullet1)
            sprites_list.remove(bullet1)
            bullet1_count = 0

    for bullet2 in bullet2_list:
        player1_hit = pygame.sprite.spritecollide(bullet2, player1_list, False)
        bullet2_hits_wall = pygame.sprite.spritecollide(
            bullet2, walls_list, False)

        for player1 in player1_hit:
            bullet2_list.remove(bullet2)
            sprites_list.remove(bullet2)
            player1_hp -= 1
            bullet2_count = 0
            if player1_hp == 0:
                sprites_list.empty()
                winner = 2

        for wall in bullet2_hits_wall:
            walls_list.remove(bullet2)
            sprites_list.remove(bullet2)
            bullet2_count = 0

    # CREATES GRAPHICS
    screen.fill(black)
    if winner == 1 or winner == 2:
        win_text = myfont.render("Player " + str(winner) + " Wins!", 1, white)
        win_rect = win_text.get_rect(center=(width / 2, 158))
        screen.blit(win_text, win_rect)

    sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
