import os

class Canvas:
    def __init__(self, width, height):
        self.allowed_canvas_sizes = [i for i in range(1, 101)]
        if width not in self.allowed_canvas_sizes or height not in self.allowed_canvas_sizes:
            raise CanvasException("Length of canvas side must be integer between 1 and 100")
        self._x = width
        self._y = height

        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWallX(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x

    def hitsWallY(self, point):
        return round(point[1]) < 0 or round(point[1]) >= self._y

    # Set the given position to the provided character on the canvas
    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    # Clear the terminal (used to create animation)
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Clear the terminal and then print each line in the canvas
    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))