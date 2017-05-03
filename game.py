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
screen_rect = screen.get_rect()
screen_rect.height = screen_rect.height - 100
screen_rect = screen_rect.move((0, 100))
pygame.display.set_caption('Penguin Rescue')
pygame.display.set_icon(pygame.image.load('assets/images/gui/penguin_icon.png').convert_alpha())


# Set Color Constants
PALE_BLUE = 208, 236, 253
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 2, 2)


def pquit():
    pygame.quit()
    exit()


def draw_sprites(all_sprites):
    for sprite in all_sprites:
        screen.blit(sprite.img, (sprite.rect.x, sprite.rect.y))


# need a function to update HUD (score, etc)
def hud(score):
    pass


def game_over(player):
    player.rect = (0,0,0,0)
    player.kill()
    print("Game Over!")
    return 'credits'

def rescue_penguin(score, player, penguin):
    score += 1
    penguin.rect = (0, 0, 0, 0)
    penguin.kill()
    return score

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

    player, penguin, yeti, snowball = GameObjects.spawn_sprites(screen_rect)
    all_sprites = pygame.sprite.RenderUpdates(player, penguin, yeti, snowball)
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
                    elif event.key == pygame.K_SPACE:
                        game_stage = 'credits'

                elif game_stage == 'credits':
                    if event.key == pygame.K_SPACE:
                        pquit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0


        if game_stage == 'game':
            player.rect.x += x_change
            player.rect.y += y_change

            # check for collision with sides of game area
            if player.rect.left < screen_rect.left:
                player.rect.left = screen_rect.left
            elif player.rect.right > screen_rect.right:
                player.rect.right = screen_rect.right
            elif player.rect.top < screen_rect.top:
                player.rect.top = screen_rect.top
            elif player.rect.bottom > screen_rect.bottom:
                player.rect.bottom = screen_rect.bottom
            else:
                pass

            # check for collision with monsterm, if so then end game
            if player.rect.colliderect(yeti.rect):
                game_stage = game_over(player)
            # check for collision with target sprite
            # the player should get one point for each target sprite rescued(hit)
            elif player.rect.colliderect(penguin.rect):
                score = rescue_penguin(score, player, penguin)
                print(score)
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
