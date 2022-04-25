import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, width, height, color):
        self.height = height
        self.width = width
        self.color = color

    def make(self, canvas_name):
        canvas = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        canvas[:] = self.color
        img = Image.fromarray(canvas, 'RGB')
        img.save(canvas_name)

class Square:

    def __init__(self, X, Y, side, color):
        self.side = side
        self.color = color
        self.X = X
        self.Y = Y

    def make(self, canvas):
        square = np.zeros((self.side, self.side, 3), dtype=np.uint8)


class Rectangle:

    def __init__(self, X, Y, width, height, color):
        self.color = color
        self.height = height
        self.width = width
        self.Y = Y
        self.X = X

    def make(self, canvas):
        pass


canvas = Canvas(200, 200, (255,255,255))
canvas.make('canvas.png')
