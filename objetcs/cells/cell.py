"""Класс клетки, от которого будут наследоваться объекты"""
import pygame


class Cell(pygame.sprite.Sprite):

    def __init__(self, board, size, coords, *group):
        super().__init__(*group)

        self.board = board
        self.size = size
        self.board.cells[coords[0]][coords[1]] = self

        self.rect = self.image.get_rect()
        self.rect.x = coords[0] * size
        self.rect.y = coords[1] * size
