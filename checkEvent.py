import pygame
def check_event():
    '''
    Отслеживает нажатые клавиши
    :return: None
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()