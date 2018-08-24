import pygame

from entities.Block import Block
from resources.Consts import Consts as c


class Player(Block):
    def __init__(self, img=c.player_img[0]):
        Block.__init__(self, img=img)

    def move(self, event, block_positions):
        pos = self.rect.copy()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.image = c.player_img[2]
                pos.x -= c.BLOCK[0]

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.image = c.player_img[3]
                pos.x += c.BLOCK[0]

            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.image = c.player_img[0]
                pos.y += c.BLOCK[1]

            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                self.image = c.player_img[1]
                pos.y -= c.BLOCK[1]

            if not self.in_map(block_positions, pos):
                self.set_position(pos)

    def set_position(self, pos):
        if pos.left <= c.BLOCK[0]:
            pos.left = c.BLOCK[0]

        if pos.right >= c.WINDOW[0] - c.BLOCK[0]:
            pos.right = c.WINDOW[0] - c.BLOCK[0]

        if pos.top <= c.BLOCK[1]:
            pos.top = c.BLOCK[1]

        if pos.bottom >= c.WINDOW[1] - c.BLOCK[1]:
            pos.bottom = c.WINDOW[1] - c.BLOCK[1]

        self.rect = pos

    @staticmethod
    def in_map(block_positions, pos):
        for position in enumerate(block_positions):
            if position[1][0] == pos.x and position[1][1] == pos.y:
                return True

        return False
