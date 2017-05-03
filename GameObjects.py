import pygame
import random

def load_sprite_img(img):
    image = pygame.image.load(img)
    return image, image.get_rect()


def spawn_sprites(screen_rect):
    # need a function to spawn target sprites and monsters
    player = Player()
    player.area = screen_rect

    penguin = Penguin()
    penguin.rect.x = random.randint(20, (screen_rect.width - 20))
    penguin.rect.y = random.randint(20, (screen_rect.height - 20))
    penguin.area = screen_rect

    yeti = Yeti()
    yeti.rect.x = random.randint(20, (screen_rect.width - 20))
    yeti.rect.y = random.randint(20, (screen_rect.height - 20))
    yeti.area = screen_rect

    snowball = Snowball()

    return player, penguin, yeti, snowball


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img, self.rect = load_sprite_img('assets/images/sprites/player.png')
        self.speed = 5
        self.area = None

    def update(self):
        pass

    def move(self, num):
        if num == 1:
            newpos = self.rect.move((0, -self.speed))
        elif num == 2:
            newpos = self.rect.move((0, self.speed))
        elif num == 3:
            newpos = self.rect.move((-self.speed, 0))
        elif num == 4:
            newpos = self.rect.move((self.speed, 0))
        self.rect = newpos


class Penguin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img, self.rect = load_sprite_img('assets/images/sprites/penguin.png')
        self.area = None

    def update(self):
        pass


class Snowball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img, self.rect = load_sprite_img('assets/images/sprites/small_snowball.png')

    def update(self):
        pass


class Yeti(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img, self.rect = load_sprite_img('assets/images/sprites/yeti.png')
        self.speed = 20
        self.area = None

    def update(self):
        # ultimately we want the yeti to chase the player
        # don't want the yeti to go off screen or be able to pass
        # through any obstacles

        x_change = 0
        y_change = 0

        dir_change = random.randint(1, 4)
        if dir_change == 1:
            y_change = self.speed
        elif dir_change == 2:
            y_change = -self.speed
        elif dir_change == 3:
            x_change = self.speed
        elif dir_change == 4:
            x_change = -self.speed
        else:
            pass

        newpos = self.rect.move((x_change, y_change))

        # this checks for collisions against sides of game area
        if newpos.bottom > self.area.bottom:
            y_change = - y_change
        if newpos.top < self.area.top:
            y_change = - y_change
        if newpos.right < self.area.right:
            x_change = - x_change
        if newpos.left > self.area.left:
            x_change = - x_change

        # need to check for collision with other objects


        newpos = self.rect.move((x_change, y_change))
        self.rect = newpos


class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img, self.rect = load_sprite_img('assets/images/sprites/small_snowball.png')

    def update(self):
        pass


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img, self.rect = load_sprite_img('assets/images/sprites/player.png')
        self.speed = 5
        self.area = None

