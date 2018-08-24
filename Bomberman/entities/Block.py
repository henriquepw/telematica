from pygame import sprite, Surface

from resources.Consts import Consts as c


class Block(sprite.Sprite):
    def __init__(self, x=c.BLOCK[0], y=c.BLOCK[1], img=c.block_img):
        sprite.Sprite.__init__(self)
        # self.image = Surface([c.BLOCK[0], c.BLOCK[1]])
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_coordinate(self, x, y):
        self.rect.x = x
        self.rect.y = y
