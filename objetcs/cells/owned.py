"""Индикатор захваченной клетки"""


from objetcs.cells.cell import Cell
from imagelib.load import load_image


class OwnedCell(Cell):

    def __init__(self, board, size, coords, owner, *group):
        if owner == "r":
            self.image = load_image("owned_by_red_cell.png", (size, size))
            name = "Owned_by_red"
        elif owner == "b":
            self.image = load_image("owned_by_blue_cell.png", (size, size))
            name = "Owned_by_blue"
        super().__init__(board, size, coords, name, *group)

    def update(self):
        pass