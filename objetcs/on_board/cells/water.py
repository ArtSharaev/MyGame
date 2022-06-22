"""Вода"""


from objetcs.on_board.cell import Cell
from imagelib.load import load_image


class WaterCell(Cell):

    def __init__(self, board, size, coords, *group):
        self.image = load_image("water1.png", (size, size))
        name = "water"
        super().__init__(board, size, coords, name, *group)

    def update(self):
        pass