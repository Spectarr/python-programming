import re
import sys
from tkinter import messagebox, Button, Tk, Text, Label, END
import turtle as t

MULTIPLY = 20
root = Tk()
root.withdraw()


def prepare_instructions(raw_data):
    fix_data = []
    sub_pattern = re.compile("\n|\s|[,|;|\.]$")
    for figure in raw_data:
        raw_data = re.sub(sub_pattern, "", figure)
        fix_data.append(raw_data)

    instructions = []
    for instruction_list in fix_data:
        instruction_list = re.split("(?<=\))[,|;]", instruction_list)
        for i, coord in enumerate(instruction_list):
            coord = re.sub("\(|\)", "", coord)
            coord = coord.replace(",", ".")
            print(coord)
            if not coord:
                continue
            try:
                instruction_list[i] = [
                    float(i) * MULTIPLY for i in re.split(";|,", coord)
                ]
            except ValueError:
                print("Check the data", coord)
                continue
        instructions.append(instruction_list)
    print(instructions)
    return instructions


def get_xy(coord: list):
    if not coord:
        return
    try:
        x, y = coord
        return x, y
    except ValueError:
        print(f"unable to unpack: {coord}")


def draw(coords):
    t.penup()
    first_coord = get_xy(coords[0])
    if not first_coord:
        return
    t.goto(first_coord)
    t.pendown()
    for coord in coords:
        coord = get_xy(coord)
        if not coord:
            continue
        t.goto(get_xy(coord))


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        win.destroy()
        sys.exit()


def process(instructions):
    root.quit()
    instructions = prepare_instructions(instructions)

    t.shape("arrow")
    t.speed("slow")
    t.pensize(3)

    for instruction in instructions:
        draw(instruction)

    t.penup()
    t.hideturtle()
    t.mainloop()


def add():
    messages = text_box.get("1.0", "end-1c")
    print(f"adding: {messages}")

    messages = messages.split("и")
    for message in messages:
        message = re.sub("[а-я|А-Я]|:|\.", "", message)
        instructions.append(message)
    label.config(text=f"added {len(instructions)} elements")
    text_box.delete("1.0", END)


def clear_data():
    global instructions
    instructions = []
    label.config(text=f"data cleared")


if __name__ == "__main__":
    win = Tk()
    win.protocol("WM_DELETE_WINDOW", on_closing)
    win.geometry("350x150+560+200")
    win.title("Нарисуй слона")
    text_box = Text(
        win, height=5, width=48, background="light grey", border=3, font=("Courier", 8)
    )
    instructions = []
    button_add = Button(win, text="Add", command=add)
    button_draw = Button(win, text="Draw", command=lambda: process(instructions))
    button_clear = Button(win, text="Clear", command=clear_data)
    button_exit = Button(win, text="Exit", command=quit)
    label = Label(win, text="")
    text_box.grid(column=0, columnspan=4, row=0)
    button_add.grid(column=0, row=1)
    button_draw.grid(column=1, row=1)
    button_clear.grid(column=2, row=1)
    button_exit.grid(column=3, row=1)
    label.grid(columnspan=4, column=0, row=2)
    win.mainloop()
