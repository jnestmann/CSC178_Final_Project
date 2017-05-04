import pygame
import random


def load_sprite_img(img):
    image = pygame.image.load(img)
    return image, image.get_rect()


def spawn_sprites(game_area):
    # need a function to spawn target sprites and monsters
    player = Player()
    player.area = game_area

    penguins = pygame.sprite.Group()

    for _ in range(30):
        penguin = Penguin()
        penguin.rect.x = random.randint(0, game_area.width-penguin.rect.width)
        penguin.rect.y = random.randint(100, game_area.height)
        penguin.area = game_area
        penguins.add(penguin)

    yeti = Yeti()
    yeti.rect.x = random.randint(0, game_area.width)
    yeti.rect.y = random.randint(100, game_area.height)
    yeti.area = game_area

    return player, penguins, yeti


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img, self.rect = load_sprite_img('assets/images/sprites/player.png')
        self.speed = 5
        self.area = None
        self.score = 0

    def update(self):
        pass

    def move(self, num):
        newpos = 0
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
        self.speed = 3
        self.direction = 0
        self.dir_duration = 0

    def update(self):
        x_change = 0
        y_change = 0

        if self.direction == 1:
            y_change = self.speed
        elif self.direction == 2:
            y_change = -self.speed
        elif self.direction == 3:
            x_change = self.speed
        elif self.direction == 4:
            x_change = -self.speed
        else:
            x_change = 0
            y_change = 0

        if self.dir_duration == 0:
            self.direction = random.randint(1, 8)
            self.dir_duration = random.randint(1, 20)
        else:
            self.dir_duration -= 1


        newpos = self.rect.move((x_change, y_change))

        # this checks for collisions against sides of game area
        if newpos.bottom > self.area.bottom:
            self.direction = 2
        if newpos.top < self.area.top:
            self.direction = 1
        if newpos.right > self.area.right:
            self.direction = 4
        if newpos.left < self.area.left:
            self.direction = 3

        # need to check for collision with other objects

        newpos = self.rect.move((x_change, y_change))
        self.rect = newpos


class Yeti(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img, self.rect = load_sprite_img('assets/images/sprites/yeti.png')
        self.speed = 10
        self.area = None
        self.dir_duration = 0
        self.direction = 0


    def update(self):
        # ultimately we want the yeti to chase the player
        # don't want the yeti to go off screen or be able to pass
        # through any obstacles

        x_change = 0
        y_change = 0

        if self.direction == 1:
            y_change = self.speed
        elif self.direction == 2:
            y_change = -self.speed
        elif self.direction == 3:
            x_change = self.speed
        elif self.direction == 4:
            x_change = -self.speed
        else:
            pass

        if self.dir_duration == 0:
            self.direction = random.randint(1, 4)
            self.dir_duration = random.randint(1, 10)
        else:
            self.dir_duration -= 1


        newpos = self.rect.move((x_change, y_change))

        # this checks for collisions against sides of game area
        if newpos.bottom > self.area.bottom:
            self.direction = 2
        if newpos.top < self.area.top:
            self.direction = 1
        if newpos.right > self.area.right:
            self.direction = 4
        if newpos.left < self.area.left:
            self.direction = 3

        # need to check for collision with other objects

        newpos = self.rect.move((x_change, y_change))
        self.rect = newpos


class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img, self.rect = load_sprite_img('assets/images/sprites/small_snowball.png')

    def update(self):
        pass
