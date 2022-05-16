"""Клеточное поле"""


class Board:
    def __init__(self, size):
        # создаем массив с клетками
        self.cells = []
        for i in range(size[0]):
            arr = []
            for j in range(size[1]):
                arr.append(None)
            self.cells.append(arr)

    def render(self):
        pass
