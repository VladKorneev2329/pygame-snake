import pygame
from colors import *


def check_event():
    """
    Отслеживает нажатые клавиши
    :return: None
    """
    global snake_directions

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
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
snake_size = []
snake_directions = {
    'direction_up': True,
    'direction_down': False,
    'direction_right': False,
    'direction_left': False
}

pygame.init()
display = pygame.display.set_mode(display_size)
pygame.display.set_caption(display_title)

for row in range(display_height // display_pixel):
    for col in range(display_width // display_pixel):
        if (row + col) % 2 == 0:
            color = color_thistle
        else:
            color = color_silver
        pygame.draw.rect(display, color,
                         (0 + display_pixel * col, 0 + display_pixel * row, display_pixel, display_pixel))

while True:

    check_event()
    print(snake_directions)

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
        snake_y = display_height + snake_height
    elif snake_y > display_height:
        snake_y = 0

    pygame.draw.rect(display, color_lime, (snake_x, snake_y, snake_width, snake_height))

    pygame.display.flip()
    pygame.time.Clock().tick(display_fps)
