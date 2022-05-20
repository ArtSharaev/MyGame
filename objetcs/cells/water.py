"""Вода"""


from objetcs.cells.cell import Cell
from imagelib.load import load_image


class WaterCell(Cell):

    def __init__(self, board, size, coords, *group):
        self.image = load_image("water1.png", (size, size))
        name = "Water"
        super().__init__(board, size, coords, name, *group)

    def update(self):
        pass