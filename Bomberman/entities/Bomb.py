from entities.Block import Block
from resources.Consts import Consts as c


class Bomb(Block):
    def __init__(self):
        Block.__init__(self, img=c.bomb_img)
