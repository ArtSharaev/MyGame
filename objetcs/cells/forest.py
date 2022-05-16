from objetcs.cells import Cell
from imagelib import load


class ForestCell(Cell):

    def __init__(self):
        super().__init__()
        self.image = load.load_image("Cell1.png", (self.size, self.size))

    def update(self):
        pass