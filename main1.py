import pygame
from sys import exit


pygame.init()

screen = pygame.display.set_mode((800, 400))
screen.fill((20,20,20))


pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

sky_surface = pygame.image.load('Sky.png').convert()
ground_surface = pygame.image.load('Ground.png').convert()

#snail
snail_surface = pygame.image.load('snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (780,300))


test_font = pygame.font.Font('Pixeltype.ttf', 50)#first argument can be None as well if there is no specific fontstyle (None, 50)

test_surface_2 = pygame.Surface((50,50))
test_surface_2.fill((0,255,0))

text_surface = test_font.render('My game', False, (0,0,200))

#player
player_surface = pygame.image.load('player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))

snail_x_pos = 800
i = 0
x = 1
while True:
    i = i+x
    if i == 750:
        x = -1
    elif i == 0:
        x = 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #background surface
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))

######
    screen.blit(test_surface_2, (i,20))

    #text_surface
    screen.blit(text_surface, (300, 50))

    #snail
    #snail_x_pos -= 4
    #if snail_x_pos <= -100:
    #    snail_x_pos = 800
    #screen.blit(snail_surface, (snail_x_pos,264))
    snail_rect.left -= 4
    if snail_rect.left <= -100:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)


    #player
    #player_rect.top -= 1
    screen.blit(player_surface, player_rect)

    #collision
    if (player_rect.colliderect(snail_rect)):
        print("collision")


    mouse_pos = pygame.mouse.get_pos()
    #print(mouse_pos)
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())

    
    pygame.display.update()
    clock.tick(60)#max frame rate

    

    


    
    
