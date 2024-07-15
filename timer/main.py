from tkinter import *
from PIL import Image, ImageTk
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
COUNT_MIN = 5
timer = None


def countdown(count):
    minutes = math.floor(count / 60)
    secs = count % 60
    if secs < 10:
        secs = f"0{secs}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{secs}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)

def start_timer():
    main_count = COUNT_MIN * 60
    countdown(main_count)

def reset_timer():
    window.after_cancel(timer)
    label1.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")



window = Tk()
window.title("My Timer For Productivity")
window.config(pady=50, padx=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

original_image = Image.open("bomb.png")
resized_image = original_image.resize((200, 223))
image = ImageTk.PhotoImage(resized_image)

canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(90, 130, text="00:00", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

label1 = Label(text="Timer", font=(FONT_NAME, 45), fg=GREEN, bg=YELLOW, )
label1.grid(row=0, column=1)

button1 = Button(text="START", highlightbackground=YELLOW, command=start_timer)
button1.grid(row=2, column=0)

button2 = Button(text="RESET", highlightbackground=YELLOW, command=reset_timer)
button2.grid(row=2, column=2)

window.mainloop()
