"""Базовый клаcc подвижных юнитов"""

import pygame
from objetcs.base_object_on_board import BaseObjectOnBoard


class Unit(BaseObjectOnBoard):

    def __init__(self, board, size, coords, name, *group):
        super().__init__(board, size, coords, *group)
        self.name = name
        self.board.units_matrix[coords[0]][coords[1]] = self

    def __repr__(self):
        return f"{self.name.capitalize()} unit at coords {self.coords}"
