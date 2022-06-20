"""Горы"""


from objetcs.cells.cell import Cell
from imagelib.load import load_image
import random


images = ["mountain1.png", "mountain2.png", "mountain3.png"]


class MountainCell(Cell):

    def __init__(self, board, size, coords, *group):
        img = random.choice(images)
        self.image = load_image(img, (size, size))
        name = "mountain"
        super().__init__(board, size, coords, name, *group)

    def update(self):
        pass