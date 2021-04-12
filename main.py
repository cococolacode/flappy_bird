import pygame,sys

#initialize pygame
pygame.init()

#screen 
screen = pygame.display.set_mode((378, 512))
clock = pygame.time.Clock()

# Game Variables
gravity =  0.25
bird_movement = 0

# draw floor
def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,430))
    screen.blit(floor_surface,(floor_x_pos+378,430))


# load images
bg_surface = pygame.image.load("./assets/sprites/background-day.png").convert()
bg_surface = pygame.transform.scale2x(bg_surface)

#floor surface
floor_surface = pygame.image.load("./assets/sprites/base.png")
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

#bird surface
bird_surface = pygame.image.load("./assets/sprites/bluebird-midflap.png")
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center=( 100,256 ))

# pip surface



#game loop 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 12

    screen.blit(bg_surface, (0,0))
    bird_movement +=  gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface,bird_rect)
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -378:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)

