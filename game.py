import pygame
import random
import GameObjects

pygame.init()
clock = pygame.time.Clock()


bg_filenames = ('assets/images/backgrounds/bg_title.jpg',
                'assets/images/backgrounds/bg_game.jpg',
                'assets/images/backgrounds/bg_credits.jpg'
                )

music_files = ('assets/sounds/start_screen_music.wav',
               'assets/sounds/level_music.wav',
               'assets/sounds/credits_music.wav'
)

get_penguin = pygame.mixer.Sound('assets/sounds/penguin_get.wav')
hit_yeti = pygame.mixer.Sound('assets/sounds/yeti_hit.wav')
wall_hit = pygame.mixer.Sound('assets/sounds/wall_hit.wav')

game_font = 'assets/fonts/RaviPrakash-Regular.ttf'

# setup game display
size = screen_width, screen_height = 800, 700
screen = pygame.display.set_mode(size)
game_area = screen.get_rect()
game_area.height = game_area.height - 100
game_area = game_area.move((0, 100))
pygame.display.set_caption('Penguin Rescue')
pygame.display.set_icon(pygame.image.load('assets/images/gui/penguin_icon.png').convert_alpha())

# Set Color Constants
PALE_BLUE = 208, 236, 253
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 2, 2)
GREEN = (2, 255, 2)


def pquit():
    pygame.quit()
    exit()


def draw_sprites(all_sprites):
    for sprite in all_sprites:
        screen.blit(sprite.img, (sprite.rect.x, sprite.rect.y))


# need a function to update HUD (score, etc)
def hud(player):
    font = pygame.font.Font(game_font, 48)
    text = font.render(":{:0>2}".format(str(player.score)), True, WHITE)
    screen.blit(text, (60, 20))


def game_over(player, win):
    player.rect = (0, 0, 0, 0)
    if win == False:
        player.kill()
        pygame.mixer.Sound.play(hit_yeti)
        message_display("You Died!.", RED)
    else:
        message_display("Game Over", WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return 'credits'
            else:
                continue


def rescue_penguin(player, penguin):
    pygame.mixer.Sound.play(get_penguin)
    player.score += 1
    penguin.kill()


def message_display(message, color):
    font_large = pygame.font.Font(game_font, 50)
    text = font_large.render(message, True, color)
    text_rect = text.get_rect()
    screen.blit(text, (screen_width/2 - text_rect.width/2, 20))
    font_small = pygame.font.Font(game_font, 36)
    sb_text = font_small.render("Press spacebar to continue.", True, BLACK)
    sb_text_rect = sb_text.get_rect()
    screen.blit(sb_text, (screen_width/2 - sb_text_rect.width/2, 120))
    pygame.display.flip()


def pause():
    pause = True
    pygame.mixer.music.pause()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pquit()
                elif event.key == pygame.K_SPACE or event.key == pygame.K_p:
                    pause = False
        message_display("Paused", RED)
    else:
        pygame.mixer.music.play(-1)


def update_display(game_stage, all_sprites, player):
    screen.fill(PALE_BLUE)
    if game_stage == 'title':
        background = pygame.image.load(bg_filenames[0])
        screen.blit(background, (0, 0))
    elif game_stage == 'game':
        background = pygame.image.load(bg_filenames[1])
        screen.blit(background, (0, 0))
        draw_sprites(all_sprites)
        hud(player)
    elif game_stage == 'credits':
        background = pygame.image.load(bg_filenames[2])
        screen.blit(background, (0, 0))
    else:
        print("Error: Unknown game stage.")
        pquit()
    pygame.display.flip()


def game_loop():
    game_stage = 'title'  # starts with the title screen

    player, penguins, yeti = GameObjects.spawn_sprites(game_area)
    all_sprites = pygame.sprite.RenderUpdates(player, penguins, yeti)
    x_change = 0
    y_change = 0
    score = 0

    pygame.mixer.music.load('assets/sounds/Start_screen_music.wav')
    pygame.mixer.music.play(-1)

    play = True

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pquit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pquit()

                elif game_stage == 'title':
                    if (event.key == pygame.K_SPACE or
                                event.key == pygame.K_p):
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('assets/sounds/level_music.wav')
                        pygame.mixer.music.play(-1)
                        game_stage = 'game'
                    elif event.key == pygame.K_q:
                        game_stage = 'credits'
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('assets/sounds/credits_music.wav')
                        pygame.mixer.music.play(-1)

                elif game_stage == 'game':
                    if event.key == pygame.K_UP:
                        y_change -= player.speed
                    elif event.key == pygame.K_DOWN:
                        y_change += player.speed
                    elif event.key == pygame.K_LEFT:
                        x_change -= player.speed
                    elif event.key == pygame.K_RIGHT:
                        x_change += player.speed
                    elif event.key == pygame.K_p:
                        pause()

                elif game_stage == 'credits':
                    if event.key == pygame.K_SPACE:
                        pquit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

            if event.type == pygame.MOUSEBUTTONDOWN and game_stage == 'title':
                mousex, mousey = event.pos
                if 230 <= mousex <= 290 and 320 <= mousey <= 380:
                    game_stage = 'game'
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('assets/sounds/level_music.wav')
                    pygame.mixer.music.play(-1)

                if 560 <= mousex <= 610 and 320 <= mousey <= 380:
                    game_stage = 'credits'
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('assets/sounds/credits_music.wav')
                    pygame.mixer.music.play(-1)

        if game_stage == 'game':
            player.rect.x += x_change
            player.rect.y += y_change

            # check for collision with sides of game area
            if player.rect.left < game_area.left:
                pygame.mixer.Sound.play(wall_hit)
                player.rect.left = game_area.left
            elif player.rect.right > game_area.right:
                pygame.mixer.Sound.play(wall_hit)
                player.rect.right = game_area.right
            elif player.rect.top < game_area.top:
                pygame.mixer.Sound.play(wall_hit)
                player.rect.top = game_area.top
            elif player.rect.bottom > game_area.bottom:
                pygame.mixer.Sound.play(wall_hit)
                player.rect.bottom = game_area.bottom
            else:
                pass

            # check for collision with monster, if so then end game
            if player.rect.colliderect(yeti.rect):
                win = False
                game_stage = game_over(player, win)
            # check for collision with target sprite
            # the player should get one point for each target sprite rescued(hit)
            elif pygame.sprite.spritecollideany(player, penguins):
                penguin = pygame.sprite.spritecollideany(player, penguins)
                rescue_penguin(player, penguin)
            elif pygame.sprite.spritecollideany(yeti, penguins):
                penguin = pygame.sprite.spritecollideany(yeti, penguins)
                chance_to_eat = random.randint(1, 20)
                if chance_to_eat == 20:
                    penguin.kill()
                else:
                    pass
            elif penguins.sprites() == []:
                win = True
                game_stage = game_over(player, win)
            else:
                pass

        # check for collision with obstacles
        # obstacles typically just prevent forward movement, but may want to

        # add the ability later for different effects on the player
        # like spawning additional monsters, reducing health, score, etc

        all_sprites.update()
        update_display(game_stage, all_sprites, player)
        clock.tick(60)

    pquit()


if __name__ == '__main__':
    game_loop()
