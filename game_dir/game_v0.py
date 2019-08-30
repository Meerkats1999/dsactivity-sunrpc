import rpyc
import pygame
import random

connect = rpyc.connect("localhost",1025)
pygame.init()
myFont = pygame.font.SysFont("monospace", 35)

clock=pygame.time.Clock()
enemy_size=50
player_size=50
frames=60

width=1280
height=720

SPEED=5
player_pos=[int(width/2),height-player_size]
BLUE=(0,0,255)
BCK_COLOR = (0,0,0)

count=10
RED=(255,0,0)

enemy_list=[]

screen=pygame.display.set_mode((width,height))

game_over=False
score=0
def detect_collision(player_pos, enemy_pos):
        p_x = player_pos[0]
        p_y = player_pos[1]
        e_x = enemy_pos[0]
        e_y = enemy_pos[1]
        if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
            if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
                return True
        return False

def collision_check(enemy_list, player_pos):
        for enemy_pos in enemy_list:
            if detect_collision(enemy_pos, player_pos):
                return True
        return False
def enemy_spawn(e_list,num):
    if len(e_list)<num:
        x_pos=random.randint(0,width-enemy_size)
        y_pos=random.randint(0,360)
        e_list.append([x_pos,y_pos])

def make_enemies(e_list):
    for enemy in e_list:
        pygame.draw.rect(screen,RED,(enemy[0],enemy[1],enemy_size,enemy_size))

def update_enemy_pos(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < height:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1
    return score

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            x= player_pos[0]
            y=player_pos[1]
            if event.key == pygame.K_LEFT:
                x-=50
            if event.key == pygame.K_RIGHT:
                x+=50
            if event.key == pygame.K_UP:
                y-=50
            if event.key == pygame.K_DOWN:
                y+=50
            player_pos=[x,y]

        if event.type == pygame.QUIT:
            exit()
            
    screen.fill((BCK_COLOR))
    make_enemies(enemy_list)
    score = update_enemy_pos(enemy_list, score)
    SPEED = connect.root.set_level(score, SPEED)

    text = "Score:" + str(score) + " HighScore: " + str(connect.root.high_score())
    label = myFont.render(text, 1, RED)
    screen.blit(label, (width-800, height-80))

    pygame.draw.rect(screen,BLUE,(player_pos[0],player_pos[1],player_size,player_size))
    enemy_spawn(enemy_list,count)
    update_enemy_pos(enemy_list,score)
    if collision_check(enemy_list, player_pos):
        game_over = True
        connect.root.send_score(score)

    make_enemies(enemy_list)

    clock.tick(frames)

    pygame.display.update()