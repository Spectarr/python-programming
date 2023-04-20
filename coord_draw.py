import re


def menu():
    print("\nInput draw instructions:")
    instructions = []
    while True:
        add_ = input("Input instructions or press Enter to Draw")
        if add_ == "":
            break
        instructions.append(add_)
    return instructions

    if menu_choice == "1":
        data.insert(menu_choice.split(","))
    return menu_choice


figure1 = """(0;-4); (1;-8); (2;-8); (2;-2); (4;-8); (5;-8); (4;2); (3;3); (4;5); (4;7); (3;8); (2;10);
(1;8); (-2;6); (-4;6); (-2;3); (-1;2); (-4;0);(-5;-2); (-5;-5); (-7;-5); (-9;-6); (-10;-7);
(-10;-8); (-9;-9); (-7;-10); (-3;-10); (-2;-9); (-4;-8); (-6;-8); (-7;-7);(-6;-6);(-5;-6);
(-3;-8); (1;-8); (0;-7); (-2;-7); (-1;-7); (0;-6); (0;-4); (-1;-3); (-2;-3)"""
figure2 = """(4; - 3), (4; - 5), (3; - 9), (0; - 8), (1; - 5), (1; - 4), (0; - 4), (0; - 9), (- 3; - 9),
(- 3; - 3), (- 7; - 3), (- 7; - 7), (- 8; - 7), (- 8; - 8), (- 11; - 8), (- 10; - 4), (- 11; - 1),
(- 14; - 3),
(- 12; - 1), (- 11;2), (- 8;4), (- 4;5)."""
figure3 = """(2; 4),(6; 4)."""
data = []
data.append(figure1)
data.append(figure2)
data.append(figure3)
drawing = []

for figure in data:
    data = re.sub("\n|\.|\s", "", figure)
    drawing.append(data)

print(drawing)


def prepare_coords(data, multiply):
    coords = []
    for instruction in data:
        instruction = re.split(",|(?<=\));", instruction)
        for coord in instruction:
            coord = re.sub("\(|\)|\n", "", coord)
            coords.append([int(i) * multiply for i in re.split(";|,", coord)])

    print(coords)


prepare_coords(drawing, 10)


def draw(coords):
    import turtle as t

    t.shape("arrow")
    t.speed("fast")
    t.penup()
    t.pensize(3)
    t.goto(coords[0])
    t.pendown()

    for coord in coords:
        try:
            x, y = coord
            t.goto(x, y)
        except ValueError:
            print(coord)
            pass

    t.penup()
    t.hideturtle()
    t.mainloop()
