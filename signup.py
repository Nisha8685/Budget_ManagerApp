import tkinter
from tkinter import ttk
from tkinter import messagebox
import csv
from save import *



def log(window):
    window.deiconify()

def signup(window):


    signup_window = tkinter.Toplevel(window)
    signup_window.title("Sign UP Information Page")

    frame1=tkinter.Frame(signup_window,background="lightblue")
    frame1.pack()

    firstnamelabel = tkinter.Label(frame1, text="Enter your First Name:", bg='Blue',
                                fg='black')
    firstnamelabel.grid(row=0, column=0, padx=10, pady=10)

    firstnametxt = tkinter.Entry(frame1, bg='white')
    firstnametxt.grid(row=0, column=1, padx=10, pady=10)

    lastnamelabel = tkinter.Label(frame1, text="Enter your Last Name:", bg='Blue',
                                   fg='black')
    lastnamelabel.grid(row=1, column=0, padx=10, pady=10)

    lastnametxt = tkinter.Entry(frame1, bg='white')
    lastnametxt.grid(row=1, column=1, padx=10, pady=10)

    user_idlabel = tkinter.Label(frame1, text="Enter User ID:", bg='Blue',
                                   fg='black')
    user_idlabel.grid(row=2, column=0, padx=10, pady=10)

    user_idtxt = tkinter.Entry(frame1, bg='white')
    user_idtxt.grid(row=2, column=1, padx=10, pady=10)

    passwordlabel = tkinter.Label(frame1, text="Enter Password:", bg='Blue',
                                   fg='black')
    passwordlabel.grid(row=3, column=0, padx=10, pady=10)

    passwordtxt = tkinter.Entry(frame1, bg='white')  # Set entry background color
    passwordtxt.grid(row=3, column=1, padx=10, pady=10)

    confirmpasswordlabel = tkinter.Label(frame1, text="Confirm Password:", bg='Blue',fg='black')  # Set label background and foreground color
    confirmpasswordlabel.grid(row=4, column=0, padx=10, pady=10)

    confirmpasswordtxt = tkinter.Entry(frame1, bg='white')  # Set entry background color
    confirmpasswordtxt.grid(row=4, column=1, padx=10, pady=10)

    securityquestionLabel=tkinter.Label(frame1,text="Please select on security question for recovery",bg="Blue",fg="Black")
    securityquestionLabel.grid(row=5,column=0,padx=10,pady=10)

    securityquestioncombo = ttk.Combobox(frame1, values=['What is your favourite sport?', 'What is your pet name?', 'What is your home country'])
    securityquestioncombo.grid(row=5, column=1, padx=10, pady=10)

    securityanswertxt = tkinter.Entry(frame1, bg='white')  # Set entry background color
    securityanswertxt.grid(row=5, column=2, padx=10, pady=10)




    savebutton=tkinter.Button(signup_window,text="Save and Log In",command=lambda :save(firstnametxt,lastnametxt,user_idtxt,passwordtxt,confirmpasswordtxt,securityquestioncombo,securityanswertxt,window))
    savebutton.pack()

