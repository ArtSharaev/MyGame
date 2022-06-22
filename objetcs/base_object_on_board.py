""""Базовый класс для всех объектов на поле"""

import pygame


class BaseObjectOnBoard(pygame.sprite.Sprite):

    def __init__(self, board, size, coords, *group):
        super().__init__(*group)

        self.board = board
        self.size = size
        self.coords = coords
        self.rect = self.image.get_rect()
        self.rect.x = coords[0] * size
        self.rect.y = coords[1] * size