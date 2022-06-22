"""Базовый класс клетки"""

import pygame
from objetcs.base_object_on_board import BaseObjectOnBoard


class Cell(BaseObjectOnBoard):

    def __init__(self, board, size, coords, name, *group):
        super().__init__(board, size, coords, *group)
        self.name = name
        if self.name != "selected":
            self.board.cells_matrix[coords[0]][coords[1]] = self

    def __repr__(self):
        return f"{self.name.capitalize()} cell at coords {self.coords} with side {self.size}"
