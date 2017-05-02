import pygame

class GameDisplay:
    pass

class Screen(GameDisplay):
    size = screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Penguin')
    pygame.display.set_icon(pygame.image.load('assets/images/penguin_icon.png').convert_alpha())

    background = pygame.image.load(bg_filenames[0])
    screen.blit(background, (0, 0))