"""Индикатор захваченной клетки"""


from objetcs.on_board.indicator import Indicator
from imagelib.load import load_image


class OwnedCell(Indicator):

    def __init__(self, board, size, coords, owner, *group):
        if owner == "r":
            self.image = load_image("owned_by_red_cell.png", (size, size))
            name = "owned_by_red"
        elif owner == "b":
            self.image = load_image("owned_by_blue_cell.png", (size, size))
            name = "owned_by_blue"
        super().__init__(board, size, coords, name, *group)

    def update(self):
        pass