"""Клеточное поле"""


class Board:
    def __init__(self, size_x, size_y):
        # создаем массив с клетками
        self.cells = []
        for i in range(size_x):
            arr = []
            for j in range(size_y):
                arr.append(None)
            self.cells.append(arr)


    def render(self):