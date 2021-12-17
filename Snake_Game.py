import pygame
import random

pygame.init()


# Color specification
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

def plot_snake(gameWindow, color, snake_list):
    snake_size = 30
    for list in snake_list:
        for x, y in list:
            pygame.draw.rect(gameWindow, color, [x,y,snake_size,snake_size])

# define font module
font = pygame.font.SysFont(None, 60)

def text_screen(text, color, x , y):
    screen_text = font.render(text,True, color)
    gameWindow.blit(screen_text, [x,y])

# defining clock
clock = pygame.time.Clock()
# setting display size
display_width = 700
display_height = 600
gameWindow = pygame.display.set_mode((display_width,display_height))
# setting Title of window
pygame.display.set_caption("Snake Game")

def apple_position(snake_list):
    apple_x = random.randint(15, display_width - 15)
    apple_y = random.randint(15, display_height - 15)
    for list in snake_list:
        if abs(apple_x-list[0][0]) < 16 and abs(apple_y-list[0][1]) < 16:
            apple_position(snake_list)
    else:
        return [apple_x,apple_y]

# catching every event on/over window
def game_loop():
    # Game specific variables
    game_exit = False
    game_over = False
    velocity_x = 0
    velocity_y = 0
    snake_x = random.randint(0,display_width)
    snake_y = random.randint(0,display_height)
    score = 0
    speed = 5
    
    apple_size = 30
    snake_list = []
    snake_length = 1

    head = []
    head.append([snake_x, snake_y])
    
    snake_list.append(head)
    apple = apple_position(snake_list)
    fps = 60

    while not game_exit:
        # everything that needs to be updated is in this loop
        for event in pygame.event.get():
            # if event is an pressing of quit button
            if event.type == pygame.QUIT:
                game_exit = True
            # if event is a pressing of any key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if velocity_x != -speed:
                        velocity_x = speed
                        velocity_y = 0
                elif event.key == pygame.K_LEFT:
                    if velocity_x != speed:
                        velocity_x = -speed
                        velocity_y = 0
                elif event.key == pygame.K_DOWN:
                    if velocity_y != -speed:
                        velocity_y = speed
                        velocity_x = 0
                elif event.key == pygame.K_UP:
                    if velocity_y != speed:
                        velocity_y = -speed
                        velocity_x = 0
        
        head = []
        snake_x += velocity_x
        snake_y += velocity_y
        head.append([snake_x, snake_y])
        snake_list.append(head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        plot_snake(gameWindow, black, snake_list)
        # if snake eats apple
        if abs(apple[0] - snake_x) < 20 and abs(apple[1] - snake_y) <20:
            score += 1 
            apple = apple_position(snake_list)
            snake_length += speed
        # drawing apple 
        pygame.draw.rect(gameWindow, red, [apple[0], apple[1], apple_size, apple_size])
        
        # keeping the snake in the screen
        if snake_x < 0:
            snake_x = display_width
        elif snake_x >= display_width:
            snake_x = 0
        if snake_y < 0:
            snake_y = display_height
        elif snake_y >= display_height:
            snake_y = 0
        
        text_screen("Score: " + str(score), red, 5, 5)
        pygame.display.update()
        # Filling background 
        gameWindow.fill(white)
        clock.tick(fps)
game_loop()
pygame.quit()
quit()
