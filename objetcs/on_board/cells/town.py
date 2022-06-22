"""Город"""


from objetcs.on_board.cell import Cell
from imagelib.load import load_image
import random


images = ["town1.png", "town2.png"]


class TownCell(Cell):

    def __init__(self, board, size, coords, *group):
        img = random.choice(images)
        self.image = load_image(img, (size, size))
        name = "town"
        super().__init__(board, size, coords, name, *group)

    def update(self):
        pass