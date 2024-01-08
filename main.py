from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timmer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timmer)
    canvas.itemconfig(time_text,text="00:00")
    timer.config(text = "Timer")
    check_mark.config(text="")

    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timmer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
       global timmer
       timmer = window.after(1000, count_down, count - 1)
    else:
        start_timmer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            check_mark.config(text="✔")


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
timer.grid(column=1, row=0)
timer.config(padx=5, pady=5)

check_mark = Label(fg=GREEN, bg=YELLOW, font=("Arial", 15, "bold"))
check_mark.grid(column=1, row=4)
check_mark.config(padx=5, pady=5)

start = Button(text="Start", command=start_timmer)
start.grid(column=0, row=3)
start.config(padx=5, pady=5)

reset = Button(text="Reset", command=reset)
reset.grid(column=2, row=3)
reset.config(padx=5, pady=5)

window.mainloop()
