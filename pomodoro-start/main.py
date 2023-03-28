from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text="00:00")
    timer_label.config(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
    check_mark.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        timer_label.config(text="WORK TIME", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
        timer_label.grid(column=1, row=0)
        countdown(work_sec)
    elif reps == 8:
        timer_label.config(text="LONG BREAK", fg=RED, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
        timer_label.grid(column=1, row=0)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="SHORT BREAK", fg=PINK, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
        timer_label.grid(column=1, row=0)
        countdown(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    print(count)
    count_min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{sec} ")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✓"

        check_mark.config(text=marks, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()
