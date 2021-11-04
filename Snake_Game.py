import pygame

pygame.init()

# Game specific variables
game_exit = False
game_over = False
display_width = 700
display_height = 600
velocity_x = 0
velocity_y = 0
snake_x = 10
snake_y = 10
snake_size = 15
fps = 30

# Color specification
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

# defining clock
clock = pygame.time.Clock()
# setting display size
gameWindow = pygame.display.set_mode((display_width,display_height))
# setting Title of window
pygame.display.set_caption("Snake Game")
# catching every event on/over window
while not game_exit:
    for event in pygame.event.get():
        # if event is an pressing of quit button
        if event.type == pygame.QUIT:
            game_exit = True
        # if event is a pressing of any key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 5
                velocity_y = 0
            elif event.key == pygame.K_LEFT:
                velocity_x = -5
                velocity_y = 0
            elif event.key == pygame.K_DOWN:
                velocity_y = 5
                velocity_x = 0
            elif event.key == pygame.K_UP:
                velocity_y = -5
                velocity_x = 0
    
    # creating a rectangle
    snake_x += velocity_x
    snake_y += velocity_y
    pygame.draw.rect(gameWindow,black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    # Filling background 
    gameWindow.fill(white)
    clock.tick(fps)

pygame.quit()
quit()