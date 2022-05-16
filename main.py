import pygame
from objetcs.cells.field import FieldCell
from objetcs.cells.forest import ForestCell
from objetcs.board import Board


CELL_SIZE = 100
BOARD_DIMENSIONS = (17, 9)


if __name__ == '__main__':
    gameboard = Board(BOARD_DIMENSIONS)

    pygame.init()
    size = (BOARD_DIMENSIONS[0] * CELL_SIZE, BOARD_DIMENSIONS[1] * CELL_SIZE)
    screen = pygame.display.set_mode(size)
    pygame.display.flip()
    all_sprites = pygame.sprite.Group()

    for y in range(BOARD_DIMENSIONS[1]):
        for x in range(BOARD_DIMENSIONS[0]):
            FieldCell(gameboard, CELL_SIZE, (x, y), all_sprites)

    running = True
    while running:
        all_sprites.draw(screen)
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()