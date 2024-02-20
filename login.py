import tkinter
import tkinter.messagebox
from tkinter import ttk
from tkinter import messagebox
import csv
from adddeleteedit import *
from report import *
from statistics import *


def login(UserIDtxt, Passwordtxt,window):
    user_id = UserIDtxt.get()
    password = Passwordtxt.get()

    def update(salary_label, salarytxt, business_label, businesstxt, online_label, onlinetxt):
        global totalincome
        salary = int(salarytxt.get())
        business = int(businesstxt.get())
        online = int(onlinetxt.get())
        totalincome = (salary + business + online)
        budget = [user_id, salary, business, online, totalincome]

        with open("income.csv", "w") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(budget)

        # salary_label.pack_forget()
        # salarytxt.pack_forget()
        # business_label.pack_forget()
        # businesstxt.pack_forget()
        # online_label.pack_forget()
        # onlinetxt.pack_forget()

        totalbudgetvaluelabel.config(text=totalincome)

    def setbudget():
        salary_label = tkinter.Label(summery_frame, text="Salary income")
        salary_label.grid(row=2, column=0, padx=10, pady=10)

        salarytxt = tkinter.Entry(summery_frame)
        salarytxt.grid(row=2, column=1, padx=10, pady=10)

        business_label = tkinter.Label(summery_frame, text="Business income")
        business_label.grid(row=3, column=0, padx=10, pady=10)

        businesstxt = tkinter.Entry(summery_frame)
        businesstxt.grid(row=3, column=1, padx=10, pady=10)

        online_label = tkinter.Label(summery_frame, text="Online income")
        online_label.grid(row=4, column=0, padx=10, pady=10)

        onlinetxt = tkinter.Entry(summery_frame)
        onlinetxt.grid(row=4, column=1, padx=10, pady=10)

        update_button = tkinter.Button(summery_frame, text="Update your total budget",
                                       command=lambda: update(salary_label, salarytxt, business_label, businesstxt,
                                                              online_label, onlinetxt), bg="Blue", fg="black")
        update_button.grid(row=5, column=0, padx=10, pady=10)

    with open("UserIDinfo.csv", "r") as filewrirer:
        csvreader = csv.reader(filewrirer)
        logged_in = False
        for row in csvreader:
            if len(row) >= 5:  # Ensure row has enough elements
                if row[2] == user_id:
                    if row[3] == password:
                        logged_in = True
                        break
                    else:
                        messagebox.showerror("Error", message="You have entered wrong login credentials")
                        return  # Exit the function if login fails

        if logged_in:
            messagebox.showinfo("Logged On", message="You have logged in successfully")

            # Create the main menu window
            MainMenu_window = tkinter.Toplevel(window)
            MainMenu_window.title("Main Menu Page")

            MainMenu_frame = tkinter.Frame(MainMenu_window)
            MainMenu_frame.pack()

            message_label = tkinter.Label(MainMenu_frame,
                                          text="Hello " + row[0] + " " + row[1] + " Welcome Back!!!!!!!",
                                          font=("Arial", 12), bg="Blue", fg="Pink")
            message_label.pack()

            Account_frame = tkinter.LabelFrame(MainMenu_frame, text="DashBoard", bg='Pink', width=5000,
                                               height=1000)  # Set frame background color
            Account_frame.pack()
            accountbutton = tkinter.Button(Account_frame, text="Add/Delete/Edit expences",
                                           command=lambda: adddeleteedit(user_id,window), bg='Blue',
                                           fg='black')
            accountbutton.pack()
            reportbutton = tkinter.Button(Account_frame, text="Reports", command=lambda :reports(user_id), bg='Blue',
                                          fg='black')
            reportbutton.pack()
            statisticbutton = tkinter.Button(Account_frame, text="Statistics", command=statistics, bg="Blue",
                                             fg="Black")
            statisticbutton.pack()

            summery_frame = tkinter.LabelFrame(MainMenu_frame, text="Summery", bg='Pink', width=500,
                                               height=1000)  # Set frame background color
            summery_frame.pack()

            setincome_button = tkinter.Button(summery_frame, text="Set your total budget", command=setbudget, bg="Blue",
                                              fg="black")
            setincome_button.grid(row=1, column=0, padx=10, pady=10)
            totalbudgetlabel = ttk.Label(summery_frame,
                                         text="Total Budget:")  # Set label background and foreground color
            totalbudgetlabel.grid(row=6, column=0, padx=10, pady=10)

            with open("income.csv", "r") as filereader:
                csvreader = csv.reader(filereader)
                for row in csvreader:
                    totalincome = 0
                    if len(row) >= 5:
                        if row[0] == user_id:
                            totalincome = int(row[4])
                            totalbudgetvaluelabel = ttk.Label(summery_frame, text=totalincome)
                            totalbudgetvaluelabel.grid(row=6, column=1, padx=10, pady=10)

            totalexpenceslabel = ttk.Label(summery_frame, text="Total Expences:")
            totalexpenceslabel.grid(row=7, column=0, padx=10, pady=10)
            with open("expenses.csv", "r") as filereader:
                csvreader = csv.reader(filereader)
                totalexpence = 0
                for row in csvreader:
                    if len(row) >= 7:  # Ensure row has enough elements
                        if row[2] == user_id:
                            totalexpence = totalexpence + int(row[5])

                totalexpencesvaluelabel = ttk.Label(summery_frame, text=totalexpence)
                totalexpencesvaluelabel.grid(row=7, column=1, padx=10, pady=10)

            if totalexpence > totalincome:
                messagebox.showwarning("Alert Message", message="You have exceeded the set budget.")
            elif totalexpence < totalincome:
                messagebox.showwarning("Alert Message", message="You are all good in budget")
            else:
                messagebox.showwarning("Alert Message",
                                       message="Your expences are same as your set budget.Do not spend more")





