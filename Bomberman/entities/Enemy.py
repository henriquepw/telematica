from random import randrange, choice

import pygame

from entities.Player import Player
from resources.Consts import Consts as c


def collide(pos, list_position_block):
    for positon in enumerate(list_position_block):
        if positon[1] == pos:
            return True
    return False


class Enemy(Player):
    def __init__(self, block_positions):
        Player.__init__(self, img=c.enemy_img[0])

        list_block_positions = block_positions + c.not_block_positions
        self.appear = 0

        count = 0
        while count != len(list_block_positions):
            count = 0
            for i in list_block_positions:
                if i[0] == self.rect.x and i[1] == self.rect.y:
                    self.rect.x = randrange(c.BLOCK[0], c.WINDOW[0] - c.BLOCK[0], c.BLOCK[0])
                    self.rect.y = randrange(c.BLOCK[1], c.WINDOW[1] - c.BLOCK[1], c.BLOCK[1])
                else:
                    count += 1

    def direction(self, block_positions):
        while True:
            key = choice([pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT])
            pos = self.mov(key)
            if not self.in_map(block_positions, pos):
                self.set_image(key)
                self.set_position(pos)
                break

    def mov(self, key):
        pos = self.rect.copy()
        if key == pygame.K_LEFT:
            pos.x -= c.BLOCK[0]
        elif key == pygame.K_RIGHT:
            pos.x += c.BLOCK[0]
        elif key == pygame.K_DOWN:
            pos.y += c.BLOCK[1]
        elif key == pygame.K_UP:
            pos.y -= c.BLOCK[1]

        return pos

    def set_image(self, key):
        if key == pygame.K_LEFT:
            self.image = c.enemy_img[2]
        elif key == pygame.K_RIGHT:
            self.image = c.enemy_img[3]
        elif key == pygame.K_DOWN:
            self.image = c.enemy_img[0]
        elif key == pygame.K_UP:
            self.image = c.enemy_img[1]

    @staticmethod
    def in_map(block_positions, pos):
        for position in enumerate(block_positions):
            if position[1][0] == pos.x and position[1][1] == pos.y:
                return True
        return False
