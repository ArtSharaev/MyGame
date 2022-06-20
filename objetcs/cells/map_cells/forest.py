"""Лес"""


from objetcs.cells.cell import Cell
from imagelib.load import load_image


class ForestCell(Cell):

    def __init__(self, board, size, coords, *group):
        self.image = load_image("forest1.png", (size, size))
        name = "forest"
        super().__init__(board, size, coords, name, *group)

    def update(self):
        pass