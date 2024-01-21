from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip,json

WHITE = "#F5EDCE"
BLACK = "#1A0000"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for char in range(randint(8, 10))]

    password_list += [choice(symbols) for char in range(randint(2, 4))]

    password_list += [choice(numbers) for char in range(randint(2, 4))]


    shuffle(password_list)

    password = "".join(password_list)
    pswd_entry.delete(0,END)
    pswd_entry.insert(index=0,string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Method 1:

#pswd_dict = {
#    "website":[""],
#    "email":[""],
#    "password":[""]
#}
#
#def save_passwd():
#    pswd_dict["website"][0] = web_entry.get()
#    pswd_dict["email"][0] = mail_entry.get()
#    pswd_dict["password"][0] = pswd_entry.get()
#
#    paswd_df = pandas.DataFrame(pswd_dict)
#    
#    #default W mode,now in append mode,header false mean keys are not printed
#    paswd_df.to_csv("./passwd.csv",mode='a',header=False) 
#
#    web_entry.delete(0,END)
#    mail_entry.delete(0,END)
#    pswd_entry.delete(0,END)
# Method 2

def save_passwd():
    website = web_entry.get().upper()
    email = mail_entry.get()
    password = pswd_entry.get()
    new_item = {
        website:{
        "Email":email,
        "Password":password
        }
    }

    if len(email)>0 and len(password)>0:
        is_ok = messagebox.askokcancel(title=website,message=f"Email: {email}\nPassword: {password}\nPress OK to save.")
        if is_ok:
            try:
                with open("data.json",'r') as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    json.dump(new_item,data_file,indent=4)
            else:
                data.update(new_item)

                with open("data.json","w") as data_file:
                    json.dump(data,data_file,indent=4)
            finally:

                web_entry.delete(0,END)
                pswd_entry.delete(0,END)
    else:messagebox.showerror(title="Error",message="Can't leave email or password empty.")

#----------------------------- Search Password -------------------------#
def search():
    try:
        with open("data.json",'r') as data_file:
            data = json.load(data_file)
    except:
        messagebox.showerror(title="Problem",message="No data file found.")
    else:
        website = web_entry.get().upper()

        if len(website) > 0:
            try:
                email = data[website]['Email']
                password = data[website]['Password']
            except KeyError:
                messagebox.showerror(title="Problem",message="Password not found.")
            else:
                messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
                pyperclip.copy(data[website]['Password'])
        else:
            messagebox.showerror(title="Problem",message="Put something in the box.")

# ---------------------------- UI SETUP ------------------------------- #

#setting Root window
root_window = Tk()
root_window.title("Password Manager")
root_window.configure(bg=WHITE,padx=50,pady=50)

# Applied Canvas and Logo
logo_canvas = Canvas(width=200,height=200,highlightthickness=0,bg=WHITE)
img = PhotoImage(file="./logo.png")
logo_canvas.create_image(100,100,image=img)
logo_canvas.grid(column=1,row=0)

# Adding label,entries and buttons.

web_label = Label(text="Website:",fg=BLACK,bg=WHITE,font=("Arial",10,"bold"))
web_label.grid(column=0,row=1)

web_entry = Entry(width=32)
web_entry.grid(column=1,row=1,columnspan=2,sticky="w")

search_button = Button(text="Search",width=14,command=search)
search_button.grid(column=2,row=1,sticky='w')

mail_label = Label(text="Email/Username:",fg=BLACK,bg=WHITE,font=("Arial",10,"bold"))
mail_label.grid(column=0,row=2)

mail_entry = Entry(width=51)
mail_entry.insert(0,"shubhra@gmail.com")
mail_entry.grid(column=1,row=2,columnspan=2,sticky="w")

pswd_label = Label(text="Password:",fg=BLACK,bg=WHITE,font=("Arial",10,"bold"))
pswd_label.grid(column=0,row=3)

pswd_entry = Entry(width=32)
pswd_entry.grid(column=1,row=3,sticky="w")

generate_button = Button(text="Generate Password",command=gen_password)
generate_button.grid(column=2,row=3,sticky='w')

add_button = Button(text="Add",width=42,command=save_passwd)
add_button.grid(column=1,row=4,columnspan=2)



root_window.mainloop()