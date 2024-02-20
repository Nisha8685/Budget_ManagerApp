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



def FPassword(event):
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

    frame2 = tkinter.Frame(forgotpassword_window)
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



window = tkinter.Tk()
window.title("Budget Manager")

# Set background image
# bg_image = tkinter.PhotoImage(file="background_image.png")
# bg_label = tkinter.Label(window, image=bg_image)
# bg_label.place(relwidth=1, relheight=1)


frame = tkinter.Frame(window)
frame.pack()

logininfoframe = tkinter.LabelFrame(frame, text="Login Page", bg='Pink',width=5000,height=1000)  # Set frame background color
logininfoframe.grid(row=0, column=0, sticky="news",padx=10,pady=10)

UserIDlabel = tkinter.Label(logininfoframe, text="User ID:", bg='Blue', fg='black')  # Set label background and foreground color
UserIDlabel.grid(row=0, column=0, padx=10, pady=10)

UserIDtxt = tkinter.Entry(logininfoframe, bg='white')  # Set entry background color
UserIDtxt.grid(row=0, column=1, padx=10, pady=10)

Passwordlabel = tkinter.Label(logininfoframe, text="Password:", bg='Blue', fg='black')  # Set label background and foreground color
Passwordlabel.grid(row=1, column=0, padx=10, pady=10)

Passwordtxt = tkinter.Entry(logininfoframe, bg='white')  # Set entry background color
Passwordtxt.grid(row=1, column=1, padx=10, pady=10)


loginbutton=tkinter.Button(window,text="Login",command=lambda :login(UserIDtxt,Passwordtxt,window),bg='Blue', fg='black')
loginbutton.pack()

signupbutton=tkinter.Button(window,text="Sign UP",command=lambda :signup(window),bg='Blue', fg='black')
# signupbutton.grid(row=1,column=1,padx=10,pady=10)
signupbutton.pack()


forgotpassword = tkinter.Label(window, text="Forgot Passwork?Click Here", fg="blue", cursor="hand2")
forgotpassword.pack()
# Bind the label to the open_link function
forgotpassword.bind("<Button-1>",FPassword)
value_label = tkinter.Label(window, text="", font=("Arial", 12))
value_label.pack()

window.mainloop()
