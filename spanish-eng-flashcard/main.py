from tkinter import *
import pandas,random,time
#Constants
BACKGROUND_COLOR = "#B1DDC6"

try:
    lang_data = pandas.read_csv("./data/to_learn.csv")
except FileNotFoundError:
    lang_data = pandas.read_csv("./data/es-en.csv")
finally:
    word_list = lang_data.to_dict(orient='records')
current_word = {}
#--------------------Generating Words----------------------#

def flip_card():

    canvas.itemconfig(canvas_background,image=en_bg_img)
    canvas.itemconfig(canvas_text,text="English",fill="white")
    canvas.itemconfig(canvas_word,text=current_word["English"],fill="white")


def gen_word():
    global current_word

    current_word = random.choice(word_list)
    canvas.itemconfig(canvas_background,image=es_bg_img)
    canvas.itemconfig(canvas_text,text="Espanol",fill="black")
    canvas.itemconfig(canvas_word,text=current_word["Espanol"],fill="black")
    root.after(3000,func=flip_card)


def is_known():
    try:
        word_list.remove(current_word)
    except ValueError: gen_word()
    else: gen_word()

#----------------------UI-Creation--------------------------#
root = Tk()
root.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
root.title("Flash card")

# Main Area
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)

es_bg_img = PhotoImage(file="./images/card_front.png")
en_bg_img = PhotoImage(file="./images/card_back.png")

canvas_background = canvas.create_image(410,263,image=en_bg_img)
canvas_text = canvas.create_text(410,63,text="Espanol-English",font=("Arial",24,"bold"),fill="white")
canvas_word =canvas.create_text(410,253,text="Press to Start",font=("Arial",48,"bold"),fill="white")

canvas.grid(column=0,row=0,columnspan=2)

# Button Configs
ri_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=ri_button_img,highlightthickness=0,command=is_known)
right_button.grid(column=1,row=1)

wr_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wr_button_img,highlightthickness=0,command=gen_word)
wrong_button.grid(column=0,row=1)


root.mainloop()

print("Done")
df = pandas.DataFrame(word_list)
df.to_csv("./data/to_learn.csv",index=False)