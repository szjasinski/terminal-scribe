import time
from termcolor import colored
import math


class AnimationScribe(TerminalScribe):
    def __init__(self, canvas, trail='.', mark='*', framerate=0.05, pos=None, degrees=90, trail_color='black',
                 mark_color='red', bold=False, blink=False, reverse=False):
        super().__init__(canvas)
        self.allowed_colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'light_grey',
                               'dark_grey',
                               'light_red', 'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan']

        self.allowed_signs = [chr(i) for i in range(32, 127)]
        self.allowed_framerates = [i*0.01 for i in range(1, 101)]

        is_pos_list_len_2 = False
        if isinstance(pos, list):
            if len(pos) == 2:
                is_pos_list_len_2 = True
        self.is_pos_allowed = (is_pos_list_len_2 and 0 <= pos[0] < canvas._x and 0 <= pos[1] < canvas._y) or pos is None

        self.allowed_degrees = [i for i in range(360)]

        if not isinstance(canvas, Canvas):
            raise ScribeException("Canvas argument must be Canvas object")
        if trail not in self.allowed_signs:
            raise ScribeException("Trail must be ASCII between 32 and 126")
        if mark not in self.allowed_signs:
            raise ScribeException("Mark must be ASCII between 32 and 126")
        if framerate not in self.allowed_framerates:
            raise ScribeException("Frame rate must be between 0.01 and 1 and must be a multiplication of 0.01")
        if not self.is_pos_allowed:
            raise ScribeException("Position (pos) must be inside the canvas")
        if degrees not in self.allowed_degrees:
            raise ScribeException("Degrees must be between 0 and 359")
        if trail_color not in self.allowed_colors:
            raise ScribeException("Wrong trail color. Must be in: \n\n" + str(self.allowed_colors) + "\n")
        if mark_color not in self.allowed_colors:
            raise ScribeException("Wrong mark color. Must be in: \n\n" + str(self.allowed_colors) + "\n")
        if not isinstance(bold, bool) or not isinstance(blink, bool) or not isinstance(reverse, bool):
            raise ScribeException("Arguments bold, blink and reverse must be bool type.")

        self.trail = trail
        self.mark = mark
        self.framerate = framerate
        self.pos = pos
        if self.pos is None:
            self.pos = [0, 0]

        radians = degrees / 180 * math.pi
        self.direction = [math.sin(radians), -math.cos(radians)]
        self.trail_color = trail_color
        self.mark_color = mark_color
        self.attrs = []
        if bold:
            self.attrs.append('bold')
        if blink:
            self.attrs.append('blink')
        if reverse:
            self.attrs.append('reverse')

    def set_trail(self, trail):
        self.trail = trail

    def set_mark(self, mark):
        self.mark = mark

    def set_framerate(self, framerate):
        self.framerate = framerate

    def set_color(self, color):
        self.trail_color = trail_color

    def draw(self, pos):
        self.canvas.setPos(self.pos, colored(self.trail, self.trail_color, attrs=self.attrs))
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, self.mark_color, attrs=self.attrs))
        self.canvas.print()
        time.sleep(self.framerate)

    def draw_snail(self, size):
        size = size - 1
        a = [270, 0, 90, 180]
        lines_num = 2*size-1
        self.set_degrees(90)
        self.forward(size)
        self.set_degrees(180)
        for i in range(0, 2*lines_num):
            self.forward(size - i)
            self.set_degrees(a[2*i % 4])
            self.forward(size - i)
            self.set_degrees(a[(2*i+1) % 4])