
class Canvas:

    def __init__(self, width, height, color):
        self.height = height
        self.width = width
        self.color = color

class Square:

    def __init__(self, X, Y, side, color):
        self.color = color
        self.X = X
        self.Y = Y

    def make(self, canvas):
        pass

class Rectangle:

    def __init__(self, X, Y, width, height, color):
        self.color = color
        self.height = height
        self.width = width
        self.Y = Y
        self.X = X

    def make(self, canvas):
        pass

