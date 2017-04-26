class GameObjects:
    def __init__(self, x=0, y=0, width=0, height=0, img=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img


class Penguin(GameObjects):
    pass


class Snowball(GameObjects):
    pass


class Snowman(GameObjects):
    pass
