import pygame
import os
import sys
current_path =os.path.dirname(__file__)
os.chdir(current_path)
pygame.init()
WIDHT = 1801
HEIGHT = 801
screen = pygame.display.set_mode((WIDHT, HEIGHT))
fps = 60
clock = pygame.time.Clock()
list_player = []
Num_HOD = 0
font =pygame.font.SysFont('Aria', 40)
plika_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

maps_list =[
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
]

class Plitka(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = on_image
        self.rect =self.image.get_rect()
        self.rect.topleft=pos
        self.on=True
        self.adr =(self.rect.y // 100, self.rect.x //100)
    def update(self):
        if pygame.sprite.spritecollideany(self ,player_group , False):
            self.on =False
            self.image =of_image
            maps_list[self.adr[0]][self.adr[1]]=1
        pos =pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.on:
                if self.rect.left <pos[0] < self.rect.right and
class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y, name):
        pygame.sprite.Sprite.__init__(self)
        self.image =image
        self.rect =self.image.get_rect()
        self.rect.x =x
        self.rect.y = y
        self.hod = False
        self.step =False
        self.name = name

on_image =pygame.image.load('data/image/on.png').convert_alpha()
of_image =pygame.image.load('data/image/of.png').convert_alpha()
p_1_image =pygame.image.load('data/image/P_1.png').convert_alpha()
p_2_image =pygame.image.load('data/image/p_2.png').convert_alpha()

player_1 =Player(p_1_image, 10 ,10, '1')
player_group.add(player_1)
list_player.append(player_1)
player_2 =Player(p_2_image, 610 ,610, '2')
player_group.add(player_2)
list_player.append(player_2)
list_player[0].hod =True



def game():
    screen.fill('grey')
    plika_group.update()
    plika_group.draw(screen)
    player_group.update()
    player_group.draw(screen)

    if len(player_group) == 1:
        text = f'win player: {list_player[0].name}'
    else:
        text = f'Ход игрока- {list_player[Num_HOD].name}'
    text_render = font.render(text , 'black', True)
    screen.blit(text_render,(0,0))
    pygame.display.update()



def drawmaps():
    for i in range(0,7):
        for j in range(0,7):
            x =100 *i
            y =100 *j
            pos =(x,y)
            plika =Plitka(pos)
            plika_group.add(plika)

drawmaps()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()
    game()
    clock.tick(fps)

