from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_TIME = 15
SHORT_BREAK_TIME = 5
LONG_BREAK_TIME = 10
rep=0
symbol = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global rep,symbol
    window.after_cancel(timer)
    heading_label.config(text="Press Start",fg=GREEN,font=(FONT_NAME,26,"bold"))
    canvas.itemconfig(timer_text,text="00:00")
    rep=0
    symbol=""
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep

    rep +=1
    if rep %8 == 0:
        heading_label.config(text="Break",fg=RED,font=(FONT_NAME,40,"bold"))
        count_down(LONG_BREAK_TIME)
    elif rep%2 ==0:
        heading_label.config(text="Break",fg=PINK,font=(FONT_NAME,40,"bold"))
        count_down(SHORT_BREAK_TIME)
    else:
        heading_label.config(text="Work",fg=GREEN,font=(FONT_NAME,40,"bold"))
        count_down(WORK_TIME)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    min = math.floor(count/60)
    sec = count%60

    if sec < 10:
        sec = f"0{sec}"


    canvas.itemconfig(timer_text,text=f"{min}:{sec}")

    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        if rep %2 !=0:
            global symbol
            symbol += "✔"
            check_label.config(text=symbol)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100,pady=50,bg=YELLOW)

# Heading & ✔ Label
heading_label=Label(text="Press Start",fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
heading_label.grid(column=1,row=0)

check_label = Label(text=symbol,fg=GREEN,bg=YELLOW,font=(FONT_NAME,12,"bold"))
check_label.grid(column=1,row=2)



# Setting the image on the window
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,132,text="00:00",fill="#F9F5EB",font=(FONT_NAME,34,"bold"))
canvas.grid(column=1,row=1)

# Start & Reset button
start_button = Button(text="Start",bg="#BBD6B8",command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",bg="#BBD6B8",command=reset_timer)
reset_button.grid(column=2,row=2)

window.mainloop()