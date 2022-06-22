"""Базовый класс объектов - индикаторов"""

import pygame
from objetcs.base_object_on_board import BaseObjectOnBoard


class Indicator(BaseObjectOnBoard):

    def __init__(self, board, size, coords, name, *group):
        super().__init__(board, size, coords, *group)
        self.name = name

    def __repr__(self):
        return f"{self.name.capitalize()} indicator at coords {self.coords}"
