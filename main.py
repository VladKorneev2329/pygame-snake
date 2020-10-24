from sys import exit
from random import randrange
import pygame
from colors import *


def check_event():
    """
    Отслеживает нажатые клавиши
    :return: None
    """
    global snake_directions, snake_x, snake_y, snake_body, snake_len, score, f, food_y, food_x, display_fps

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    if keys[pygame.K_r]:
        f = False
        score = 0
        food_x = randrange(0, 39) * display_pixel
        food_y = randrange(0, 39) * display_pixel
        display_fps = 20
        snake_len = 1
        snake_body = []
        snake_x = display_width // 2
        snake_y = display_height // 2

    if keys[pygame.K_UP] or keys[pygame.K_w] and not snake_directions['direction_down']:
        snake_directions = {
            'direction_up': True,
            'direction_down': False,
            'direction_right': False,
            'direction_left': False
        }
    if keys[pygame.K_DOWN] or keys[pygame.K_s] and not snake_directions['direction_up']:
        snake_directions = {
            'direction_up': False,
            'direction_down': True,
            'direction_right': False,
            'direction_left': False
        }
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and not snake_directions['direction_left']:
        snake_directions = {
            'direction_up': False,
            'direction_down': False,
            'direction_right': True,
            'direction_left': False
        }
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and not snake_directions['direction_right']:
        snake_directions = {
            'direction_up': False,
            'direction_down': False,
            'direction_right': False,
            'direction_left': True
        }


display_size = display_width, display_height = 800, 800
display_title = 'Snake'
display_fps = 5
display_pixel = 20

snake_x = display_width // 2
snake_y = display_height // 2
snake_width = display_pixel
snake_height = display_pixel
snake_len = 1
snake_body = []
snake_directions = {
    'direction_up': True,
    'direction_down': False,
    'direction_right': False,
    'direction_left': False
}

food_x = randrange(0, 39) * display_pixel
food_y = randrange(0, 39) * display_pixel

score = 0

pygame.init()
display = pygame.display.set_mode(display_size)
pygame.display.set_caption(display_title)

while True:

    check_event()

    if snake_directions['direction_up']:
        snake_y -= display_pixel
    if snake_directions['direction_down']:
        snake_y += display_pixel
    if snake_directions['direction_right']:
        snake_x += display_pixel
    if snake_directions['direction_left']:
        snake_x -= display_pixel

    if snake_x < 0:
        snake_x = display_width
    elif snake_x > display_width - snake_width:
        snake_x = 0
    elif snake_y < 0:
        snake_y = display_height - snake_height
    elif snake_y > display_height - snake_height:
        snake_y = 0

    for row in range(display_height // display_pixel):
        for col in range(display_width // display_pixel):
            if (row + col) % 2 == 0:
                color = color_thistle
            else:
                color = color_silver
            pygame.draw.rect(display, color,
                             (0 + display_pixel * col, 0 + display_pixel * row, display_pixel, display_pixel))

    if food_x == snake_x and food_y == snake_y:
        food_x = randrange(0, 39) * display_pixel
        food_y = randrange(0, 39) * display_pixel
        display_fps += 1
        snake_len += 1
        score += 10
        print('lvl {0}'.format(score))
    display.blit(pygame.font.SysFont(None, 20).render('Очки: {0}'.format(score), True, color_red), (0, 0))
    pygame.display.update()
    snake_head = [snake_x, snake_y]
    snake_body.append(snake_head)
    if len(snake_body) > snake_len:
        del snake_body[0]
    for snake_block in snake_body[:-1]:
        if snake_block == snake_head:
            f = True
            while f:
                display.blit(
                    pygame.font.SysFont(None, 40).render('Нажмите r для рестарта, Esc для выхода', True, color_red),
                    (display_width / 5, display_height / 2))
                pygame.display.update()
                check_event()

    for snake_block in snake_body:
        pygame.draw.rect(display, color_lime, (snake_block[0], snake_block[1], snake_width, snake_height))

    pygame.display.update()

    pygame.draw.rect(display, color_red, (food_x, food_y, display_pixel, display_pixel))

    pygame.display.flip()
    pygame.time.Clock().tick(display_fps)
