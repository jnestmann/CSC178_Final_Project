import GameObjects
import pygame

pygame.init()
clock = pygame.time.Clock()

bg_filenames = ('assets/images/backgrounds/bg_title.jpg',
                'assets/images/backgrounds/bg_game.jpg',
                'assets/images/backgrounds/bg_credits.jpg'
                )

# setup game display
size = screen_width, screen_height = 800, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Penguin')
pygame.display.set_icon(pygame.image.load('assets/images/gui/penguin_icon.png').convert_alpha())

# Set Color Constants
PALE_BLUE = 208, 236, 253
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 2, 2)

penguin_img = pygame.image.load('assets/images/sprites/small_penguin.png')
penguin = GameObjects.Penguin(x=40, y=screen_height - 40, width=34, height=34, img=penguin_img)

snowman_img = pygame.image.load('assets/images/sprites/snowman.png')
snowman = GameObjects.Snowman(width=101, height=72, img=snowman_img)

snowball_img = pygame.image.load('assets/images/sprites/small_snowball.png').convert_alpha()
snowball = GameObjects.Snowball(width=34, height=34, img=snowball_img)


def pquit():
    pygame.quit()
    exit()


def game_over():
    font = pygame.font.SysFont(None, 80)
    fcolor = pygame.color.Color(5, 5, 5, 100)
    message = font.render("Game over", True, fcolor)
    screen.blit(message, (165, 100))


def draw_penguin(penguin):
    screen.blit(penguin.img, (penguin.x, penguin.y))


def update_display(game_stage):
    if game_stage == 'title':
        background = pygame.image.load(bg_filenames[0])
        screen.blit(background, (0, 0))
    elif game_stage == 'game':
        background = pygame.image.load(bg_filenames[1])
        screen.blit(background, (0, 0))
        draw_penguin(penguin)
    elif game_stage == 'credits':
        background = pygame.image.load(bg_filenames[2])
        screen.blit(background, (0, 0))
    else:
        print("Error: Unknown game stage.")
        pquit()


def game_loop():
    # update penguin position with keyboard
    x_change = 0
    y_change = 0
    game_stage = 'title'
    score = 0
    player_speed = 5

    play = True

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pquit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pquit()
                elif game_stage == 'title':
                    if event.key == pygame.K_SPACE:
                        game_stage = 'game'
                elif game_stage == 'game':
                    if event.key == pygame.K_UP:
                        y_change -= player_speed
                    elif event.key == pygame.K_DOWN:
                        y_change += player_speed
                    elif event.key == pygame.K_LEFT:
                        x_change -= player_speed
                    elif event.key == pygame.K_RIGHT:
                        x_change += player_speed
                    elif event.key == pygame.K_SPACE:
                        game_stage = 'credits'
                elif game_stage == 'credits':
                    pquit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        penguin.x += x_change
        penguin.y += y_change

        screen.fill(PALE_BLUE)
        update_display(game_stage)
        pygame.display.flip()

        clock.tick(60)

    pquit()


game_loop()
