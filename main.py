import pygame
from objetcs.cells.map_cells.field import FieldCell
from objetcs.cells.map_cells.farm import FarmCell
from objetcs.cells.map_cells.forest import ForestCell
from objetcs.cells.map_cells.water import WaterCell
from objetcs.cells.map_cells.mountain import MountainCell
from objetcs.cells.map_cells.town import TownCell
from objetcs.cells.indicators.selected import SelectedCell
from objetcs.cells.indicators.owned import OwnedCell
from objetcs.board import Board
import random


FPS = 120
CELL_SIZE = 100
BOARD_DIMENSIONS = (17, 9)
RANDOM_ARRAY = ["field", "field", "field", "field", "field", "field",
                "field", "field", "field", "field", "field", "field",
                "forest", "forest", "forest", "forest", "forest", "forest",
                "farm",
                "water", "water",
                "mountain"]


if __name__ == '__main__':
    # ЗАПУСК ИГРЫ
    gameboard = Board(BOARD_DIMENSIONS)
    pygame.init()
    size = (BOARD_DIMENSIONS[0] * CELL_SIZE, BOARD_DIMENSIONS[1] * CELL_SIZE)
    screen = pygame.display.set_mode(size)
    pygame.display.flip()
    clock = pygame.time.Clock()
    all_cells = pygame.sprite.Group()
    red_cells = pygame.sprite.Group()
    blue_cells = pygame.sprite.Group()
    selected_cells = pygame.sprite.Group()
    # рандомная генерация карты
    total_towns = int((BOARD_DIMENSIONS[0] + BOARD_DIMENSIONS[1]) / 2.5)
    towns_coords = []
    for _ in range(total_towns):
        rx = random.randrange(0, BOARD_DIMENSIONS[0])
        ry = random.randrange(0, BOARD_DIMENSIONS[1])
        while (rx, ry) in towns_coords:
            rx = random.randrange(0, BOARD_DIMENSIONS[0])
            ry = random.randrange(0, BOARD_DIMENSIONS[1])
        towns_coords.append((rx, ry))
    towns_coords = sorted(towns_coords, key=lambda c: c[0])
    towns_coords = sorted(towns_coords, key=lambda c: c[1])
    for y in range(BOARD_DIMENSIONS[1]):
        for x in range(BOARD_DIMENSIONS[0]):
            if (x, y) in towns_coords:
                TownCell(gameboard, CELL_SIZE, (x, y), all_cells)
                if (x, y) == towns_coords[0]:
                    OwnedCell(gameboard, CELL_SIZE, (x, y), "r", red_cells)
                elif (x, y) == towns_coords[-1]:
                    OwnedCell(gameboard, CELL_SIZE, (x, y), "b", red_cells)

            else:
                obj = random.choice(RANDOM_ARRAY)
                if obj == "field":
                    FieldCell(gameboard, CELL_SIZE, (x, y), all_cells)
                elif obj == "forest":
                    ForestCell(gameboard, CELL_SIZE, (x, y), all_cells)
                elif obj == "farm":
                    FarmCell(gameboard, CELL_SIZE, (x, y), all_cells)
                elif obj == "water":
                    WaterCell(gameboard, CELL_SIZE, (x, y), all_cells)
                elif obj == "mountain":
                    MountainCell(gameboard, CELL_SIZE, (x, y), all_cells)

    # ИГРОВОЙ ЦИКЛ
    running = True
    while running:
        all_cells.draw(screen)
        all_cells.update()
        red_cells.draw(screen)
        red_cells.update()
        blue_cells.draw(screen)
        blue_cells.update()
        selected_cells.draw(screen)
        selected_cells.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    cell = gameboard.get_cell(event.pos, CELL_SIZE)
                    print(cell)
            if event.type == pygame.MOUSEMOTION:
                selected_cells = pygame.sprite.Group()
                coords = gameboard.get_cell(event.pos, CELL_SIZE).coords
                SelectedCell(gameboard, CELL_SIZE, coords, selected_cells)
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()