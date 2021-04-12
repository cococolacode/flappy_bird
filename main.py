import pygame,sys, random

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

def create_pipe():
    random_pip_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (500,random_pip_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pip_pos - 300))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface,pipe)

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

# pipe surface
pipe_surface = pygame.image.load("./assets/sprites/pipe-green.png")
pipe = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [400, 600, 800]

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
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    screen.blit(bg_surface, (0,0))

    #Bird
    bird_movement +=  gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface,bird_rect)

    # Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    #floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -378:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)

