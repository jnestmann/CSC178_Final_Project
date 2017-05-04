import pygame
import GameObjects

pygame.init()
clock = pygame.time.Clock()

bg_filenames = ('assets/images/backgrounds/bg_title.jpg',
                'assets/images/backgrounds/bg_game.jpg',
                'assets/images/backgrounds/bg_credits.jpg'
                )

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
def hud(score):
    pass


def game_over(player, win):
    player.rect = (0, 0, 0, 0)
    if win == False:
        player.kill()
        message_display("You Died!.", RED)
    else:
        message_display("You saved the penguins!!!", WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return 'credits'
            else:
                continue


def rescue_penguin(player, penguin):
    player.score += 1
    penguin.kill()


def message_display(message, color):
    font_face = 'freesansbold.ttf'
    font_large = pygame.font.Font(font_face, 50)
    text = font_large.render(message, True, color)
    text_rect = text.get_rect()
    screen.blit(text, (screen_width/2 - text_rect.width/2, 20))
    font_small = pygame.font.Font(font_face, 36)
    sb_text = font_small.render("Press spacebar to continue.", True, BLACK)
    sb_text_rect = sb_text.get_rect()
    screen.blit(sb_text, (screen_width/2 - sb_text_rect.width/2, 120))
    pygame.display.flip()


def pause():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pquit()
                elif event.key == pygame.K_SPACE or event.key == pygame.K_p:
                    pause = False
        message_display("Paused", RED)


def update_display(game_stage, all_sprites, score):
    screen.fill(PALE_BLUE)
    if game_stage == 'title':
        background = pygame.image.load(bg_filenames[0])
        screen.blit(background, (0, 0))
    elif game_stage == 'game':
        background = pygame.image.load(bg_filenames[1])
        screen.blit(background, (0, 0))
        draw_sprites(all_sprites)
        hud(score)
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
                        game_stage = 'game'
                    elif event.key == pygame.K_q:
                        pquit()

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
                if 560 <= mousex <= 610 and 320 <= mousey <= 380:
                    game_stage = 'credits'

        if game_stage == 'game':
            player.rect.x += x_change
            player.rect.y += y_change

            # check for collision with sides of game area
            if player.rect.left < game_area.left:
                player.rect.left = game_area.left
            elif player.rect.right > game_area.right:
                player.rect.right = game_area.right
            elif player.rect.top < game_area.top:
                player.rect.top = game_area.top
            elif player.rect.bottom > game_area.bottom:
                player.rect.bottom = game_area.bottom
            else:
                pass

            # check for collision with monsterm, if so then end game
            if player.rect.colliderect(yeti.rect):
                win = False
                game_stage = game_over(player, win)
            # check for collision with target sprite
            # the player should get one point for each target sprite rescued(hit)
            elif pygame.sprite.spritecollideany(player, penguins):
                penguin = pygame.sprite.spritecollideany(player, penguins)
                score = rescue_penguin(player, penguin)
                print(player.score)
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
        update_display(game_stage, all_sprites, score)
        clock.tick(60)

    pquit()


if __name__ == '__main__':
    game_loop()
