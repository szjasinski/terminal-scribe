import math
from termcolor import colored


class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.05
        self.pos = [0,0]
        self.direction = [1,0]

    def set_pos(self, pos):
        self.pos = pos

    def set_degrees(self, degree):
        radians = degree / 180 * math.pi
        self.direction = [math.sin(radians), -math.cos(radians)]

    def draw(self, pos):
        # Set the old position to the "trail" symbol
        self.canvas.setPos(self.pos, self.trail)
        # Update position
        self.pos = pos
        # Set the new position to the "mark" symbol
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        # Print everything to the screen
        self.canvas.print()
        # Sleep for a little bit to create the animation
        time.sleep(self.framerate)

    def forward(self, distance=1):
        for i in range(distance):
            pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
            if self.canvas.hitsWallX(pos):
                self.direction[0] = - self.direction[0]
                pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
            if self.canvas.hitsWallY(pos):
                self.direction[1] = - self.direction[1]
                pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
            self.draw(pos)

    def up(self):
        self.direction = [0, -1]
        self.forward()

    def down(self):
        self.direction = [0, 1]
        self.forward()

    def right(self):
        self.direction = [1, 0]
        self.forward()

    def left(self):
        self.direction = [-1, 0]
        self.forward()

    def draw_square(self, size):
        for move in [self.right, self.down, self.left, self.up]:
            for i in range(size - 1):
                move()

    # n - length of the domain
    # make it possible for it to work from the data structure -- args*?????
    def draw_function(self, func, n):
        points = [[self.pos[0] + i, self.pos[1] - func(i)] for i in range(n)]
        for i in range(len(points)):
            if not self.canvas.hitsWallX(points[i]) and not self.canvas.hitsWallY(points[i]):
                self.draw(points[i])

        # _______________________________________________
        # ATTEMPT OF MAKING FUNCTIONS BOUNCE -- need to decrease values of x when hitting right wall,
        # increase when hitting left
        # CHANGE HITTING WALLS FUNCTION TO GET DATA ABOUT THE SIDE???
        # for i in range(len(points)):
        #     print(points[i])
        #     if self.canvas.hitsWallX(points[i]):
        #         for j in range(i, len(points)):
        #             points[j][0] = -points[j][0]
        #     if self.canvas.hitsWallY(points[i]):
        #         for j in range(i, len(points)):
        #             points[j][1] = -points[j][1]
        #     print(points[i])
        #     self.draw(points[i])

        # _______________________________________________
        # ATTEMPT OF MAKING IT WORK FROM DIRECTION AND FORWARD FUNCTION
        # directions = [[points[i+1][0] - points[i][0], points[i+1][1] - points[i+1][1]] for i in range(n-1)]
        # print(directions)
        #
        # for direction in directions:
        #     print(direction)
        #     dist = round(math.sqrt(direction[0]**2 + direction[1]**2))
        #     print(dist)
        #     self.forward(dist)
