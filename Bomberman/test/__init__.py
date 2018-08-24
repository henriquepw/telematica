import pygame

from entities.Game import Game
from resources.Consts import Consts as c


def main():
    game = Game()
    dead, winner, enemies = False, False, True
    while True:
        game.display.blit(c.background_img, (0, 0))

        for event in pygame.event.get():
            game.player.move(event, game.block_positions)
            game.clock.tick(30)

            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        # if enemies:
        #    threading.Thread(target=game.move_enemies).start()
        #    enemies = False

        # if pygame.sprite.groupcollide(game.gr_enemies, game.grupo_bombacollide, True, False):
        #    game.enemies -= 1

        if game.ENEMIES == 0:
            winner = True

        if pygame.sprite.groupcollide(game.gr_player, game.gr_enemies, False, False):
            dead = True

        if not dead and not winner:
            game.move_enemies()
            game.groups_update()
            game.groups_draw()

        pygame.display.update()


if __name__ == '__main__':
    main()
