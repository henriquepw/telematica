from random import randrange

from entities.Block import Block
from resources.Consts import Consts as c


class BlockDestructible(Block):
    def __init__(self, block_positions):
        Block.__init__(self, img=c.blockDestructible_img)
        list_block_positions = block_positions + c.not_block_positions

        count = 0
        while count != len(list_block_positions):
            count = 0
            for i in list_block_positions:
                if i[0] == self.rect.x and i[1] == self.rect.y:
                    self.rect.x = randrange(c.BLOCK[0], c.WINDOW[0] - c.BLOCK[0], c.BLOCK[0])
                    self.rect.y = randrange(c.BLOCK[1], c.WINDOW[1] - c.BLOCK[1], c.BLOCK[1])
                else:
                    count += 1
