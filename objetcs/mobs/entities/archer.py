"""Класс лучника"""


from objetcs.mobs.mob import Mob
from imagelib.load import load_image
import random


images = []


class Archer(Mob):

    def __init__(self, board, size, coords, *group):
        img = random.choice(images)
        self.image = load_image(img, (size, size))
        name = "archer"
        super().__init__(board, size, coords, name, *group)

    def update(self):
        pass