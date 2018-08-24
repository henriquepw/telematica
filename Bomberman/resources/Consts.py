from pygame import image


class Consts:
    # Dimensões
    NUM_OF_BLOCKS = [23, 13]
    BLOCK = [42, 44]
    WINDOW = (BLOCK[0] * NUM_OF_BLOCKS[0], BLOCK[1] * NUM_OF_BLOCKS[1])

    not_block_positions = [  # Possições que os blocos não podem ficar
        BLOCK, [BLOCK[0] * 2, BLOCK[1]], [BLOCK[0], BLOCK[1] * 2]
    ]

    map = [[0 for i in range(23)] for j in range(13)]

    # Imagens do jogo
    background_img = image.load('../resources/images/background.jpg')
    win_img = image.load('../resources/images/winner.jpeg')
    gameOver_img = image.load('../resources/images/gameOver.jpeg')
    block_img = image.load('../resources/images/block.png')
    blockDestructible_img = image.load('../resources/images/blockDestructible.jpg')
    bomb_img = image.load('../resources/images/bomb.png')

    enemy_img = [
        image.load('../resources/images/enemyDown.png'),
        image.load('../resources/images/enemyLeft.png'),
        image.load('../resources/images/enemyRight.png'),
        image.load('../resources/images/enemyUp.png')
    ]
    fire_img = [
        image.load('../resources/images/fireCenter.png'),
        image.load('../resources/images/fireDown.png'),
        image.load('../resources/images/fireLeft.png'),
        image.load('../resources/images/fireRight.png'),
        image.load('../resources/images/fireUp.png')
    ]
    player_img = [
        image.load('../resources/images/playerDown.png'),
        image.load('../resources/images/playerUp.png'),
        image.load('../resources/images/playerLeft.png'),
        image.load('../resources/images/playerRight.png')
    ]
