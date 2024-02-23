import csv
import tkinter
from tkinter import ttk
from tkinter import messagebox
from login import *


def save(firstnametxt,lastnametxt,user_idtxt,passwordtxt,confirmpasswordtxt,securityquestioncombo,securityanswertxt,window):

    fname=firstnametxt.get()
    lname=lastnametxt.get()
    user_id=user_idtxt.get()
    password=passwordtxt.get()
    confirmpassword=confirmpasswordtxt.get()
    securityquestion=securityquestioncombo.get()
    securityanswer=securityanswertxt.get()



    if fname==''or lname=='' or user_id==''or password=='' or confirmpassword=='' or securityquestion=='' or securityanswer=='':
        tkinter.messagebox.showerror("Error", message="All fields are mandatory")
    elif password!=confirmpassword:
        tkinter.messagebox.showerror("Error",message="Password doesn't match")
    else:
        with open("UserIDinfo.csv","a") as filewriter:
            csvfilewriter=csv.writer(filewriter)
            csvfilewriter.writerow([fname,lname,user_id,password,securityquestion,securityanswer])
            tkinter.messagebox.showinfo("Saving information", message="Saved")


