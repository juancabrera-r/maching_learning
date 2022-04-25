import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, width, height, color):
        self.height = height
        self.width = width
        self.color = color

        #Create a 3d numpy array of zeros
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        #Giving a color
        self.data[:] = self.color

    def make(self, canvas_name):
        img = Image.fromarray(self.data, 'RGB')
        img.save(canvas_name)

class Square:

    def __init__(self, X, Y, side, color):
        self.side = side
        self.color = color
        self.X = X
        self.Y = Y

    def draw(self, canvas):
        canvas.data[self.X: self.X + self.side, self.Y: self.Y + self.side] = self.color


class Rectangle:

    def __init__(self, X, Y, width, height, color):
        self.color = color
        self.height = height
        self.width = width
        self.Y = Y
        self.X = X

    def draw(self, canvas):
        canvas.data[self.X : self.X + self.width , self.Y : self.Y + self.height] = self.color


canvas = Canvas(20, 30, (255,255,255))
r1 = Rectangle(1,6, 10, 12, (234,252,0))
r1.draw(canvas)
s1 = Square(5,12, 3, (0,252,244))
s1.draw(canvas)
canvas.make('canvas.png')
