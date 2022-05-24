"""Класс клетки, от которого будут наследоваться объекты"""
import pygame


class Cell(pygame.sprite.Sprite):

    def __init__(self, board, size, coords, name, *group):
        super().__init__(*group)

        self.board = board
        self.size = size
        self.coords = coords
        self.name = name
        if self.name != "Selected":
            self.board.cells[coords[0]][coords[1]] = self

        self.rect = self.image.get_rect()
        self.rect.x = coords[0] * size
        self.rect.y = coords[1] * size

    def __repr__(self):
        return f"{self.name} cell at coords {self.coords} with side {self.size}"
