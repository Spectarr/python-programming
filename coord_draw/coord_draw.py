import re
import sys
from tkinter import (
    messagebox,
    Button,
    Tk,
    Text,
    Label,
    Scale,
    END,
    HORIZONTAL,
)
import turtle as t


def prepare_instructions(raw_instructions: list, scale: int):
    # remove spaces, newlines and ending symbols
    sub_pattern = re.compile("\n|\s|[,|;|\.]$")
    strip_data = [re.sub(sub_pattern, "", i) for i in raw_instructions]

    prepared_instructions = []
    for instruction_list in strip_data:
        instruction_list = re.split("(?<=\))[,|;]", instruction_list)
        for i, coord in enumerate(instruction_list):
            # remove all parantheses
            coord = re.sub("\(|\)", "", coord)
            # fix decimals
            coord = coord.replace(",", ".")
            if not coord:
                continue
            try:
                instruction_list[i] = [float(i) * scale for i in re.split(";|,", coord)]
            except ValueError:
                print("Check the data", coord)
                continue
        prepared_instructions.append(instruction_list)
    return prepared_instructions


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
        messagebox("Error", "Could not find first coordinnate")
        return
    t.goto(first_coord)
    t.pendown()
    for coord in coords:
        coord = get_xy(coord)
        if not coord:
            continue
        t.goto(get_xy(coord))


def process(scale, instructions=None):
    if not instructions:
        messagebox.showinfo("Warning", "No instructions found, add some")
        return
    instructions = prepare_instructions(instructions, scale)

    t.shape("arrow")
    t.speed("slow")
    t.pensize(3)

    for instruction in instructions:
        draw(instruction)

    t.penup()
    t.hideturtle()
    t.mainloop()


def parse_instructions(text: str) -> list:
    result = []
    messages = text.split("и")
    for message in messages:
        # remove all cyrillic symbols, dots and colons
        message = re.sub("[а-я|А-Я]|:", "", message)
        result.append(message)
    return result


class GUI:
    def __init__(self) -> None:
        self.instructions = []
        self.win = Tk()
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.win.geometry("350x200+560+200")
        self.win.title("Нарисуй по точкам")
        self.text_box = Text(
            self.win,
            height=5,
            width=48,
            background="light grey",
            border=3,
            font=("Courier", 8),
        )
        button_add = Button(self.win, text="Add", command=self.add)
        slider_label = Label(self.win, text="Scale")
        self.scale_slider = Scale(
            self.win, from_=10, to=40, length=220, tickinterval=10, orient=HORIZONTAL
        )
        self.scale_slider.set(20)
        button_draw = Button(
            self.win,
            text="Draw",
            command=lambda: process(self.scale_slider.get(), self.instructions),
        )
        button_clear = Button(self.win, text="Clear", command=self.clear_data)
        button_exit = Button(self.win, text="Exit", command=quit)
        self.label_status = Label(self.win, text="")
        self.text_box.grid(column=0, columnspan=4, row=0)
        button_add.grid(column=0, row=1)
        button_draw.grid(column=1, row=1)
        button_clear.grid(column=2, row=1)
        button_exit.grid(column=3, row=1)
        slider_label.grid(column=0, row=2)
        self.scale_slider.grid(columnspan=3, column=1, row=2)
        self.label_status.grid(columnspan=4, column=0, row=3)
        self.win.mainloop()

    def add(self):
        message = self.text_box.get("1.0", "end-1c")
        parsed = parse_instructions(message)
        self.instructions.extend(parsed)
        self.label_status.config(text=f"added {len(self.instructions)} elements")
        self.text_box.delete("1.0", END)

    def clear_data(self):
        self.instructions = []
        self.label_status.config(text=f"data cleared")

    def on_closing(self):
        self.win.destroy()
        sys.exit()


if __name__ == "__main__":
    gui = GUI()
