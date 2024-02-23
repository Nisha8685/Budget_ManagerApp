import tkinter
from tkinter import ttk
from tkinter import messagebox
import csv
import matplotlib
from openpyxl import Workbook
from tkcalendar import Calendar


from save import *
from signup import signup
from login import *

def log():
    window.deiconify()

def FPassword(event):
    window.withdraw()
    global recoverpassword
    def recover():

        with open("UserIDinfo.csv","r") as filewriter:
            csvreader=csv.reader(filewriter)
            status=False
            for row in csvreader:
                if len(row)>=6:
                    if (row[2]==IDtxt.get()):
                        if (row[4]==questioncombo.get()):
                            if (row[5]==answertxt.get()):
                                status=True
                                recoverpassword=row[3]
                                tkinter.messagebox.showinfo("Password Recovery",message="Your password recoverd successfully,Click OK")
            if status:
                message_label.config(text="Your recovered password is :" + recoverpassword)

    forgotpassword_window = tkinter.Toplevel(window)
    forgotpassword_window.title("Forgot Password")

    frame2 = tkinter.Frame(forgotpassword_window,background="lightblue")
    frame2.pack()

    IDlabel = tkinter.Label(frame2, text="Enter your User ID:", bg='Blue',
                                   fg='black')  # Set label background and foreground color
    IDlabel.grid(row=0, column=0, padx=10, pady=10)

    IDtxt = tkinter.Entry(frame2, bg='white')  # Set entry background color
    IDtxt.grid(row=0, column=1, padx=10, pady=10)

    questionLabel = tkinter.Label(frame2, text="Select and answer security question", bg="Blue",
                                          fg="Black")
    questionLabel.grid(row=2, column=0, padx=10, pady=10)

    questioncombo = ttk.Combobox(frame2, values=['What is your favourite sport?', 'What is your pet name?',
                                                         'What is your home country'])
    questioncombo.grid(row=2, column=1, padx=10, pady=10)

    answertxt = tkinter.Entry(frame2, bg='white')  # Set entry background color
    answertxt.grid(row=2, column=2, padx=10, pady=10)

    recoverbutton = tkinter.Button(frame2, text="Recover Password", command=recover, bg='Blue',fg='black')
    recoverbutton.grid(row=3,column=0,padx=10,pady=10)


    message_label = ttk.Label(frame2, text="")
    message_label.grid(row=4, column=0, padx=10, pady=10)

    logbutton = tkinter.Button(frame2, text="Go to login page", command=log, bg='Blue', fg='black')
    logbutton.grid(row=5, column=0, padx=10, pady=10)



window = tkinter.Tk()
window.title("Budget Manager")



bg_image = tkinter.PhotoImage(file="general-budget.png")

image_width = bg_image.width()
image_height = bg_image.height()

bg_label = tkinter.Label(window, image=bg_image)
bg_label.place(x=0,y=0,relheight=1,relwidth=1)  # Fill the entire window

window.geometry(f"{image_width}x{image_height}")



style = ttk.Style()
style.configure("Background.TLabelframe", background="lightblue")

# Create a main frame to hold other frames
main_frame = ttk.Frame(window,style="Background.TLabelframe")
main_frame.pack()



# Create a frame for login information
logininfoframe = ttk.LabelFrame(main_frame, text="Login Page", padding=20,style="Background.TLabelframe")
logininfoframe.pack()







# Styling for labels and entry fields
label_style = {"background": "blue", "foreground": "white", "font": ("Arial", 12)}
entry_style = {"background": "white", "foreground": "black","font": ("Arial", 12)}


# UserID Label and Entry
UserIDlabel = ttk.Label(logininfoframe, text="User ID:", **label_style)
UserIDlabel.grid(row=0, column=0, sticky="w",padx=25,pady=25)
UserIDtxt = ttk.Entry(logininfoframe, **entry_style)
UserIDtxt.grid(row=0, column=1)

# Password Label and Entry
Passwordlabel = ttk.Label(logininfoframe, text="Password:", **label_style)
Passwordlabel.grid(row=1, column=0, sticky="w")
Passwordtxt = ttk.Entry(logininfoframe, show="*", **entry_style)
Passwordtxt.grid(row=1, column=1)

# Login Button
loginbutton = ttk.Button(main_frame, text="Login",command=lambda: login(UserIDtxt, Passwordtxt, window))
loginbutton.pack(pady=20)

# Sign Up Button
signupbutton = ttk.Button(main_frame, text="Sign Up", command=lambda: signup(window))
signupbutton.pack()

# Forgot Password Label
forgotpassword = tkinter.Label(main_frame, text="Forgot Password? Click Here", fg="blue", cursor="hand2")
forgotpassword.pack(pady=10)

# Bind the label to the FPassword function
forgotpassword.bind("<Button-1>", FPassword)

# Placeholder value label
value_label = ttk.Label(main_frame, text="", font=("Arial", 12))
value_label.pack()

window.mainloop()