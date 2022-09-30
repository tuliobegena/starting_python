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
rounds = 0
checks = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global rounds
    global checks
    rounds = 0
    checks = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_label.config(text = checks*"✔")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global rounds
    global checks
    rounds += 1
    
    if rounds > 1:
        window.after_cancel(timer) # cancel the previous countdown

    if rounds % 8 == 0:
        title_label.config(text="Break", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
        rounds = 0
        checks += 1
        check_label.config(text = checks*"✔")
    elif rounds % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text="Work", fg=GREEN)
        countdown(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count): # seconds #
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    elif auto_timer.get() == 1:
       start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
auto_timer = IntVar()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT_NAME, "32"), fg=GREEN, bg=YELLOW, highlightthickness=0)
title_label.grid(column=1, row=0)

check_label = Label(text="", font=(FONT_NAME, "32"), fg=GREEN, bg=YELLOW, highlightthickness=0)
check_label.grid(column=1, row=3)


start_button = Button(text="Start", font=(FONT_NAME, "14", "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, "14", "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

auto_timer_button = Checkbutton(text="Auto-timer", variable=auto_timer, onvalue=1, offvalue=0, font=(FONT_NAME, "14", "bold"), bg=YELLOW, highlightthickness=0)
auto_timer_button.grid(column=2, row=3)


window.mainloop()