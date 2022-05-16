from objetcs.cells.cell import Cell
from imagelib.load import load_image


class ForestCell(Cell):

    def __init__(self, board, size, coords, *group):
        self.image = load_image("Cell1.png", (size, size))
        super().__init__(board, size, coords, *group)

    def update(self):
        pass