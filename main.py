import os
import time
from termcolor import colored
import math
import threading





def run_scribe_family(family):

    canvas = Canvas(25, 25)
    for scr in family:
        scr['scribe'] = TerminalScribe(canvas)
        scr['scribe'].set_pos(scr['pos'])
        scr['scribe'].set_degrees(scr['degrees'])

    # move n-th scribe from a family
    def move_scribe(n, family):
        scribe = family[n]['scribe']
        fs = [move['function'] for move in family[n]['moves']]
        args = [move['arg'] for move in family[n]['moves']]

        for f, arg in zip(fs, args):
            if f == 'draw_square':
                scribe.draw_square(arg)
            if f == 'set_degrees':
                scribe.set_degrees(arg)
            if f == 'forward':
                scribe.forward(arg)

    threads = [threading.Thread(target=move_scribe, args=(n, family)) for n in range(len(family))]
    [t.start() for t in threads]


# run_scribe_family(scribe_family)

broseidons = 69


def big_tangens(x):
    return 6*math.tan(x/6)


canvas = Canvas(20,20)
scribe = AnimationScribe(canvas, trail="x", framerate=0.02, trail_color='yellow',
                 mark_color='blue', bold=True, blink=True, reverse=True)


f = math.tan
n = 40
# scribe.set_pos([3,15])

# scribe.draw_function(big_tangens,n)

canvas.clear()
scribe.draw_snail(1)
