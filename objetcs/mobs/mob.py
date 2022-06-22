""""Базовый класс для всех подвижных существ"""

import pygame


class Mob(pygame.sprite.Sprite):

    def __init__(self, board, size, coords, name, *group):
        super().__init__(*group)

        self.board = board
        self.size = size
        self.coords = coords
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.x = coords[0] * size
        self.rect.y = coords[1] * size

    def move(self, coords):
        pass