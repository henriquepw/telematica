import time

import pygame
from pygame.sprite import Group

from entities.Block import Block
from entities.BlockDestructible import BlockDestructible
from entities.Enemy import Enemy
from entities.Player import Player
from resources.Consts import Consts as c


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Bomberman")

        self.BLOCKS_DESTRUCTIBLE = 100
        self.ENEMIES = 10
        self.appear = 0

        self.display = pygame.display.set_mode(c.WINDOW)
        self.clock = pygame.time.Clock()

        self.player = Player()
        self.block_positions = []

        self.gr_player = Group()
        self.gr_enemies = Group()
        self.gr_block = Group()
        self.gr_block_destructible = Group()
        self.gr_bomb = Group()
        self.gr_bomb_collide = Group()

        self.start()

    def start(self):
        self.groups_empty()

        self.gr_player.add(self.player)
        self.set_block()
        self.set_block_destructible()
        self.set_enemies()

        for m in c.map:
            print("\n " + m.__str__())

    def groups_draw(self):
        self.gr_player.draw(self.display)
        self.gr_enemies.draw(self.display)

        self.gr_block.draw(self.display)
        self.gr_block_destructible.draw(self.display)

        self.gr_bomb.draw(self.display)
        self.gr_bomb_collide.draw(self.display)

    def groups_update(self):
        self.gr_player.update()
        self.gr_enemies.update()

        self.gr_block.update()
        self.gr_block_destructible.update()

        self.gr_bomb.update()
        self.gr_bomb_collide.update()

    def groups_empty(self):
        self.gr_player.empty()
        self.gr_enemies.empty()
        self.gr_block.empty()
        self.gr_block_destructible.empty()
        self.gr_bomb.empty()
        self.gr_bomb_collide.empty()

    def set_enemies(self):
        for i in range(self.ENEMIES):
            enemy = Enemy(self.block_positions)
            self.gr_enemies.add(enemy)

    def set_block(self):
        count_y = 0
        for y in range(c.BLOCK[1] * 2, c.WINDOW[1] - (c.BLOCK[1] * 2), c.BLOCK[1]):
            if count_y % 2 == 0:
                count_x = 0
                for x in range(c.BLOCK[0] * 2, c.WINDOW[0] - (c.BLOCK[0] * 2), c.BLOCK[0]):
                    if count_x % 2 == 0:
                        block = Block(x, y)
                        c.map[int(y / c.BLOCK[1] - 1)][int(x / c.BLOCK[0] - 1)] = 1
                        self.block_positions.append([block.rect.x, block.rect.y])
                        self.gr_block.add(block)
                    count_x += 1

            count_y += 1

    def set_block_destructible(self):
        for i in range(self.BLOCKS_DESTRUCTIBLE):
            b = BlockDestructible(self.block_positions)
            c.map[int(b.rect.y / c.BLOCK[1] - 1)][int(b.rect.x / c.BLOCK[0] - 1)] = 2

            self.block_positions.append([b.rect.x, b.rect.y])
            self.gr_block_destructible.add(b)

    def game_over(self):
        self.display.blit(c.gameOver_img, ((c.WINDOW[0] - 750) // 2, (c.WINDOW[1] - 510) // 2))

    def win(self):
        self.display.blit(c.win_img, ((c.WINDOW[0] - 750) // 2, (c.WINDOW[1] - 510) // 2))

    def move_enemies(self):
        while True:
            for enemy in self.gr_enemies:
                enemy.direction(self.block_positions)
            time.sleep(1)

            '''self.appear += 1
    if self.appear % 13 == 0:
        for enemy in self.gr_enemies:
            enemy.direction(self.block_positions)
    if self.appear == 30:
        self.appear = 0'''
