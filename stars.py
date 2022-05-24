import turtle as t
from random import randint, random

t.shape('turtle')

t.speed('fastest')


def draw_star(points, size, star_color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(star_color)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

# Основной код
t.Screen().bgcolor('dark blue')
WIDTH, HEIGHT = [1280, 900]
t.Screen().setup(WIDTH, HEIGHT)

while True:
    random_points  = randint(2, 5) * 2 + 1
    random_size = randint(10, 100)
    random_color = (random(), random(), random())
    random_x = randint(-WIDTH//2, WIDTH//2)
    random_y = randint(-HEIGHT//2, HEIGHT//2)
    draw_star(random_points, random_size, random_color, random_x, random_y) 

t.hideturtle()
t.mainloop()   