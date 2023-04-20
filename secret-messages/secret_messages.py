import sys
import string
from tkinter import messagebox, simpledialog, Button, Tk, Text

root = Tk()
root.withdraw()

ALPHABETS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ALPHABETS += ALPHABETS.lower()
ALPHABETS += string.ascii_letters


def is_even(number):
    return number % 2 == 0


def get_even_letters(message):
    return [v for i, v in enumerate(message) if is_even(i)]


def get_odd_letters(message):
    return [v for i, v in enumerate(message) if not is_even(i)]


def rotate(alph, n):
    first = alph[:n]
    second = alph[n:]
    return second + first


def caesar_cypher(message, n):
    result = ""
    rot = rotate(ALPHABETS, n)
    for s in message:
        if not s.isalnum():
            result += s
        else:
            index = ALPHABETS.find(s)
            result += rot[index]
    return result


def swap_letters(message=None):
    if not message:
        sys.exit()
    letter_list = []
    if not is_even(len(message)):
        message += "~"
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for i in range(len(even_letters)):
        letter_list.append(odd_letters[i])
        letter_list.append(even_letters[i])
    new_message = "".join(letter_list)
    new_message.replace("~", "")
    return new_message


def get_text_box(process):

    message = text_box.get(1.0, "end-1c")
    print(message)
    messagebox.showinfo("Зашифрованное сообщение:", caesar_cypher(message, process))
    # return message


def get_message(message, operation):

    win.destroy()
    if text == "зашифровать":
        message = simpledialog.askstring("Сообщение", "Что хотите зашифровать?")
        messagebox.showinfo("Зашифрованное сообщение:", caesar_cypher(message, 8))
    elif text == "расшифровать":
        message = simpledialog.askstring(
            "Сообщение", "Введите сообщение для дешифровки:"
        )
        messagebox.showinfo("Сообщение для дешифровки:", caesar_cypher(message, -8))

    win.quit()
    return message


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        win.destroy()
        sys.exit()


if __name__ == "__main__":
    win = Tk()
    win.protocol("WM_DELETE_WINDOW", on_closing)
    win.geometry("350x150+560+200")
    win.title("Шифровка")
    text_box = Text(win, height=5, width=42, background="light grey", border=3)
    button_left = Button(win, text="зашифровать", command=lambda: get_text_box(8))
    button_right = Button(win, text="расшифровать", command=lambda: get_text_box(-8))
    button_exit = Button(win, text="выйти", command=quit)
    text_box.grid(column=0, columnspan=2, row=0)
    button_left.grid(column=0, row=1)
    button_right.grid(column=1, row=1)
    button_exit.grid(row=2, columnspan=2)

    win.mainloop()
