from hashlib import new
from operator import is_, le
from tkinter import messagebox, simpledialog, Button, Tk, LEFT, RIGHT, BOTTOM
from tracemalloc import take_snapshot
root = Tk()
root.withdraw()


def is_even(number):
    return number % 2 == 0


def get_even_letters(message):
    return [v for i, v in enumerate(message) if is_even(i)]


def get_odd_letters(message):
    return [v for i, v in enumerate(message) if not is_even(i)]


def swap_letters(message):
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


def get_message(text):
    win.destroy()
    if text == "зашифровать":
        message = simpledialog.askstring("Сообщение", "Что хотите зашифровать?")
        messagebox.showinfo("Зашифрованное сообщение:", swap_letters(message))
    elif text == "дешифровать":
        message = simpledialog.askstring("Сообщение", "Введите сообщение для дешифровки:")
        messagebox.showinfo("Сообщение для дешифровки:", swap_letters(message))
    win.quit()
    return message


if __name__ == "__main__":
    win = Tk()
    win.geometry("400x200+400+200")
    win.title("Задание")
    button_left = Button(win, text="зашифровать", command=lambda:get_message("зашифровать"))
    button_right = Button(win, text="дешифровать", command=lambda:get_message("дешифровать"))
    button_exit = Button(win, text="выйти", command=quit)
    button_left.pack(side=LEFT)
    button_right.pack(side=RIGHT)
    button_exit.pack(side=BOTTOM)
    win.mainloop()