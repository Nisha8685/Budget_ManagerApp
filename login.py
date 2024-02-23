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

        with open("income.csv", "a",newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(budget)



        totalbudgetvaluelabel.config(text=totalincome)

    def setbudget():
        salary_label = tkinter.Label(summery_frame, text="Salary income",font=40,background="grey")
        salary_label.grid(row=2, column=0, padx=10, pady=10)

        salarytxt = tkinter.Entry(summery_frame)
        salarytxt.grid(row=2, column=1, padx=10, pady=10)

        business_label = tkinter.Label(summery_frame, text="Business income",font=40,background="grey")
        business_label.grid(row=3, column=0, padx=10, pady=10)

        businesstxt = tkinter.Entry(summery_frame)
        businesstxt.grid(row=3, column=1, padx=10, pady=10)

        online_label = tkinter.Label(summery_frame, text="Online income",font=40,background="grey")
        online_label.grid(row=4, column=0, padx=10, pady=10)

        onlinetxt = tkinter.Entry(summery_frame)
        onlinetxt.grid(row=4, column=1, padx=10, pady=10)

        update_button = tkinter.Button(summery_frame, text="Update your total budget",font=40,
                                       command=lambda: update(salary_label, salarytxt, business_label, businesstxt,online_label, onlinetxt), bg="Blue", fg="black")
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
            window.withdraw()

            # Create the main menu window
            MainMenu_window = tkinter.Toplevel(window)
            MainMenu_window.title("Main Menu Page")

            screen_width = MainMenu_window.winfo_screenwidth()
            screen_height =MainMenu_window.winfo_screenheight()

            zoom_width = int(screen_width * 0.25)
            zoom_height = int(screen_height * 0.25)

            # Set window size and maximize
            MainMenu_window.geometry(f"{zoom_width}x{zoom_height}")
            MainMenu_window.attributes("-zoomed", True)

            MainMenu_frame = tkinter.Frame(MainMenu_window)
            MainMenu_frame.pack(fill=tkinter.BOTH,expand=True)

            message_label = tkinter.Label(MainMenu_frame,
                                          text="Hello " + row[0] + " " + row[1] + " Welcome Back!!!!!!!",
                                          font=("Arial", 12), bg="yellow", fg="black",foreground="blue")
            message_label.pack(fill=tkinter.BOTH)

            Account_frame = tkinter.LabelFrame(MainMenu_frame, text="DashBoard",font=50, bg='Pink', width=5000,
                                               height=1000,background="lightblue",borderwidth=2,relief="solid")
            Account_frame.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)


            accountbutton = tkinter.Button(Account_frame, text="Add/Delete/Edit expences",font=40,
                                           command=lambda: adddeleteedit(user_id,window), bg='lightblue',
                                           fg='black',width=1000)
            accountbutton.pack(fill=tkinter.Y,expand=True)
            reportbutton = tkinter.Button(Account_frame, text="Reports",font=40, command=lambda :reports(user_id), bg='lightblue',
                                          fg='black',width=1000)
            reportbutton.pack(fill=tkinter.Y,expand=True)
            statisticbutton = tkinter.Button(Account_frame, text="Statistics",font=40, command=lambda :statistics(user_id), bg="lightblue",
                                             fg="Black",width=1000)
            statisticbutton.pack(fill=tkinter.Y,expand=True)

            summery_frame = tkinter.LabelFrame(MainMenu_frame, text="Summery",font=50, bg='Pink', width=500,
                                               height=1000,borderwidth=2,relief="solid",background="lightblue")  # Set frame background color
            summery_frame.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)



            setincome_button = tkinter.Button(summery_frame, text="Set your total budget",font=40, command=setbudget, bg="Blue",
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







