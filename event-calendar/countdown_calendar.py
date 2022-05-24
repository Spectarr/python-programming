from socket import if_nameindex
from tkinter import Tk, Canvas
from datetime import date, datetime


def days_between_dates(date1, date2):
    time_between = str(date1 - date2)
    number_of_days = time_between.split(" ")
    return number_of_days[0]


def get_events():
    list_events = []
    today = datetime.today()
    pos = 60
    with open("event-calendar/events.txt", encoding="utf-8") as file:

        for line in file:
            line = line.rstrip("\n")
            current_event = line.split(",")
            event_date = datetime.strptime(current_event[1], "%d/%m/%Y")
            days_left = days_between_dates(datetime(event_date), today)
            current_event[1] = event_date
            current_event.append(days_left)
            list_events.append(current_event)
    print(list_events)
    return list_events


def get_day_suffix(num):
    num %= 10
    if num == 1:
        return "день"
    elif num in [2, 3, 4]:
        return "дня"
    else:
        return "дней"


def main():
    root = Tk()
    c = Canvas(root, width=800, height=800, bg="black")
    c.pack()
    c.create_text(
        100,
        50,
        anchor="w",
        fill="orange",
        font="Arial 50 bold",
        text="Календарь ожидания",
    )

    vertical_space = 100
    events = get_events()
    print(events)
    events.sort(key=lambda x: x[1])
    tooday = date.today()

    for event in events:
        event_name = event[0]
        days_until = days_between_dates(event[1], tooday)
        display = f"{event_name} через {days_until} {get_day_suffix(int(days_until))}"
        c.create_text(
            100,
            vertical_space,
            anchor="w",
            fill="lightblue",
            font="Arial 18",
            text=display,
        )
        vertical_space += 25

    root.mainloop()


if __name__ == "__main__":
    main()
