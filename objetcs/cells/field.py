from objetcs.cells.cell import Cell
from imagelib.load import load_image
import random


images = ["field1.png", "field2.png",
          "field3.png", "field4.png",
          "forest1.png", "forest1.png"]


class FieldCell(Cell):

    def __init__(self, board, size, coords, *group):
        img = random.choice(images)
        self.image = load_image(img, (size, size))
        super().__init__(board, size, coords, *group)

    def update(self):
        pass