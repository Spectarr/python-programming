import turtle as t
import random

from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green',
                'deep sky blue', 'blue', 'purple'])
sizes  = cycle(range(4,100))
angles = cycle(range(1,10))
shifts = cycle(range(10,1, -1))

t.shape('turtle')


def draw_circle(size, angle, shift):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(next(sizes), next(angles) , next(shifts))


t.bgcolor('black')
t.speed('fastest')
t.pensize(4)
draw_circle(30, 0,1)