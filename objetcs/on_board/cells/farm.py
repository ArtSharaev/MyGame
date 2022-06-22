"""Ферма"""


from objetcs.on_board.cell import Cell
from imagelib.load import load_image
import random


images = ["farm1.png", "farm2.png"]


class FarmCell(Cell):

    def __init__(self, board, size, coords, *group):
        img = random.choice(images)
        self.image = load_image(img, (size, size))
        name = "farm"
        super().__init__(board, size, coords, name, *group)

    def update(self):
        pass