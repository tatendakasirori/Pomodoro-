from tkinter import *
from math import floor
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
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
   
    if reps%2 ==0 and reps !=8:
        count_down(work_sec)
    if reps%8 == 0:
        count_down(short_break_sec)
    if reps > 8:
        count_down(long_break_sec)
        reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60

    # Format seconds to always show two digits
    count_sec = f"{count_sec:02}"

    text_ = f"{count_min}:{count_sec}"
    print(text_)
    canvas.itemconfig(timer_text, text=text_)

    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg = YELLOW)

canvas = Canvas(width= 200, height= 224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image= tomato_img)
timer_text = canvas.create_text(100,130, text= "00:00", fill= "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label = Label(text= "Timer", font= [FONT_NAME, "35", "bold"], fg= GREEN, bg = YELLOW)
label.grid(column= 1, row= 0)

# buttom, start and resert
start_button = Button(text= "Start", highlightthickness= 0, command= start_timer)
start_button.grid(column= 0, row= 2)

reset_button = Button(text= "Reset", highlightthickness= 0)
reset_button.grid(column= 2, row= 2)

check_marks = Label(text= "✔", fg= GREEN, bg= YELLOW)
check_marks.grid(column= 1, row= 3)




window.mainloop()