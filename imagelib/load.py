from PIL import Image
import os
import sys
import pygame


def load_image(name, size):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    im = Image.open(fullname)
    im = im.resize(size)
    im.save(fullname)
    image = pygame.image.load(fullname)
    return image
