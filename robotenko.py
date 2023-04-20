import turtle as t

t.penup()
t.speed("fast")
t.bgcolor("Dodger blue")


def rectangle(horizontal, vertical, color):
    t.shape("turtle")
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(2):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()


# feet
t.goto(-100, -150)
rectangle(50, 20, "green")
t.goto(-30, -150)
rectangle(50, 20, "purple")
# legs
t.goto(-25, -50)
rectangle(15, 100, "pink")
t.goto(-70, -50)
rectangle(15, 100, "plum")
# body
t.goto(-90, 100)
rectangle(100, 150, "gold")
# arms
t.goto(-150, 70)
rectangle(60, 15, "SkyBlue")
t.goto(-150, 110)
rectangle(15, 40, "brown")
t.goto(10, 70)
rectangle(60, 15, "orange")
t.goto(55, 110)
rectangle(15, 40, "yellow")
# neck
t.goto(-50, 120)
rectangle(15, 20, "red")
# head
t.goto(-82, 170)
rectangle(80, 50, "PaleGoldenrod")
# eyes
t.goto(-58, 160)
rectangle(30, 10, "white")
t.goto(-53, 155)
rectangle(5, 5, "black")
t.goto(-38, 155)
rectangle(5, 5, "black")
# mouth
t.goto(-63, 135)
rectangle(40, 5, "black")

t.hideturtle()
t.mainloop()
