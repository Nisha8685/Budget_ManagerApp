import tkinter
import tkinter.messagebox
from tkinter import ttk
from tkinter import messagebox
import csv
from tkcalendar import Calendar

import login
from login import *
def adddeleteedit(user_id,window):

    categories = {
            "Housing": ["Rent", "Mortgage", "Utilities", "Insurance", "Maintenance"],
            "Transportation": ["Gas", "Public Transportation", "Car Insurance", "Repairs", "Parking"],
            "Food": ["Groceries", "Dining Out", "Takeout/Delivery"],
            "Personal Care": ["Health and hygiene products", "Haircuts and salon services",
                              "Gym memberships or fitness classes", "Clothing and accessories"],
            "Healthcare": ["Health insurance premiums", "Doctor's visits", "Prescription medications", "Dental care",
                           "Vision care"],
            "Education": ["Tuition and school fees", "Books and supplies", "Educational courses or workshops",
                          "Student loan interest payments"],
            "Entertainment": ["Movies, concerts, and other entertainment events", "Hobbies and recreational activities"],

            "Miscellaneous": ["Gifts and donations", "Pet expenses", "Childcare or babysitting", "Travel expenses"]
    }

    def add_expense():
        category = category_var.get()
        subcategory = subcategory_var.get()
        amount = amount_entry.get()
        date=date_entry.get()
        with open("UserIDinfo.csv", "r") as filewrirer:
            csvreader = csv.reader(filewrirer)
            status = False
            for row in csvreader:
                if len(row) >= 5:  # Ensure row has enough elements
                    if row[2] == user_id:
                        status = True
                        break


            if status:
                firstname = row[0]
                lastname = row[1]

        # Write the expense data to a CSV file
        with open('expenses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([firstname,lastname,user_id,category, subcategory, amount,date])
        # Display a message confirming that the expense has been added
        message_label.config(text=f"Expense added: {category} - {subcategory} - ${amount}")

        # Clear the entry fields
        amount_entry.delete(0,tkinter.END)

    # Create the main window
    edit_window = tkinter.Toplevel(window)
    edit_window.title("Add/Delete or Edit your expences")

    edit_frame=tkinter.Frame(edit_window,background="lightblue")
    edit_frame.pack()


    frame1 = tkinter.LabelFrame(edit_frame,text="Add Expanse",relief="raised",background="lightblue",)
    frame1.pack(side="left",fill=tkinter.Y)

    frame2 = tkinter.LabelFrame(edit_frame,text="Edit Expense",relief="raised",background="lightblue")
    frame2.pack(side="left",fill=tkinter.Y)

    frame3 = tkinter.LabelFrame(edit_frame,text="Delete Expense",relief="raised",background="lightblue")
    frame3.pack(side="left",fill=tkinter.Y)

    # Create and place widgets in the main window
    category_label = ttk.Label(frame1, text="Category:",background="yellow")
    category_label.grid(row=0,column=0,padx=10,pady=10)

    category_var = tkinter.StringVar()
    category_dropdown = ttk.Combobox(frame1, textvariable=category_var, values=list(categories.keys()), state="readonly")
    category_dropdown.grid(row=0,column=1,padx=10,pady=10)

    subcategory_label = ttk.Label(frame1, text="Subcategory:",background="yellow")
    subcategory_label.grid(row=1,column=0,padx=10,pady=10)

    subcategory_var = tkinter.StringVar()
    subcategory_dropdown = ttk.Combobox(frame1, textvariable=subcategory_var, state="readonly")
    subcategory_dropdown.grid(row=1,column=1,padx=10,pady=10)

    amount_label = ttk.Label(frame1, text="Amount ($):",background="yellow")
    amount_label.grid(row=2,column=0,padx=10,pady=10)

    amount_entry = ttk.Entry(frame1)
    amount_entry.grid(row=2,column=1,padx=10,pady=10)


    def select_date():
        selected_date = cal.get_date()
        date_entry.delete(0, tkinter.END)
        date_entry.insert(0, selected_date)

    cal = Calendar(frame1, selectmode="day", date_pattern="dd/mm/yyyy")
    cal.grid(row=3,column=0,padx=50,pady=10,)

    setdate_button = ttk.Button(frame1, text="Set date", command=select_date)
    setdate_button.grid(row=4,column=0,padx=10,pady=10)
    date_entry = ttk.Entry(frame1)
    date_entry.grid(row=5,column=0,padx=10,pady=10)




    add_button = ttk.Button(frame1, text="Add Expense", command=add_expense)
    add_button.grid(row=6,column=0,padx=10,pady=10)

    message_label = ttk.Label(frame1, text="")
    message_label.grid(row=7,column=0,padx=10,pady=10)




    def update_subcategories(event):
        selected_category = category_var.get()
        subcategories = categories[selected_category]
        subcategory_dropdown.config(values=subcategories)

    category_dropdown.bind("<<ComboboxSelected>>", update_subcategories)

    def show_amount():

        with open("expenses.csv", "r") as filewrirer:
            csvreader = csv.reader(filewrirer)
            status = False
            for row in csvreader:
                if len(row) >= 7:
                    if row[2]== user_id:
                        if row[3] == category2_dropdown.get():
                            if row[4] == subcategory2_dropdown.get():
                                status = True
                                break

            if status:
                textbox = tkinter.Entry(frame2, width=30)
                textbox.insert(0, row[5])
                textbox.grid(row=2,column=1,padx=10,pady=10)

    def edit_amount():
        category2 = category2_dropdown.get()
        subcategory2 = subcategory2_dropdown.get()
        newamount = newamounttxt.get()


        with open("expenses.csv", 'r', newline='') as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)
            status = False
            for row in data:
                if len(row) >= 7:
                    if row[2]== user_id:
                        if row[3] == category2 and row[4] == subcategory2:
                            status = True
                            row[5] = newamount  # Assign newamount to row[5]
                            break

        if status:
            with open("expenses.csv", 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data)
            message1_label.config(text="Amount Edited")
        else:
            message1_label.config(text="Category or subcategory not found")

        newamounttxt.delete(0, tkinter.END)
    category2_label = ttk.Label(frame2, text="Category:",background="yellow")
    category2_label.grid(row=0,column=0,padx=10,pady=10)

    category2_var = tkinter.StringVar()
    category2_dropdown = ttk.Combobox(frame2, textvariable=category2_var, values=list(categories.keys()),
                                     state="readonly")
    category2_dropdown.grid(row=0,column=1,padx=10,pady=10)

    subcategory2_label = ttk.Label(frame2, text="Subcategory:",background="yellow")
    subcategory2_label.grid(row=1,column=0,padx=10,pady=10)

    subcategory2_var = tkinter.StringVar()
    subcategory2_dropdown = ttk.Combobox(frame2, textvariable=subcategory2_var, state="readonly")
    subcategory2_dropdown.grid(row=1,column=1,padx=10,pady=10)

    def update_subcategories2(event):
        selected_category = category2_var.get()
        subcategories = categories[selected_category]
        subcategory2_dropdown.config(values=subcategories)

    category2_dropdown.bind("<<ComboboxSelected>>", update_subcategories2)

    # amount2_label = ttk.Label(frame2, text="Amount ($):")
    # amount2_label.pack()
    show_button = ttk.Button(frame2, text="Show current amount", command=show_amount)
    show_button.grid(row=2,column=0,padx=10,pady=10)

    newamountlabel = tkinter.Label(frame2, text="Enter new amount:", bg='yellow',
                            fg='black')  # Set label background and foreground color
    newamountlabel.grid(row=3,column=0,padx=10,pady=10)

    newamounttxt = tkinter.Entry(frame2, bg='white')  # Set entry background color
    newamounttxt.grid(row=3,column=1,padx=10,pady=10)

    edit_button = ttk.Button(frame2, text="Edit amount", command=edit_amount)
    edit_button.grid(row=4,column=0,padx=10,pady=10)

    message1_label = ttk.Label(frame2, text="")
    message1_label.grid(row=5,column=0,padx=10,pady=10)

    def show_amount1():

        with open("expenses.csv", "r") as filewrirer:
            csvreader = csv.reader(filewrirer)
            status = False
            for row in csvreader:
                if len(row) >= 7:
                    if row[2]== user_id:
                        if row[3] == category3_dropdown.get():
                            if row[4] == subcategory3_dropdown.get():
                                status = True
                                break

            if status:
                textbox = tkinter.Entry(frame3, width=30)
                textbox.insert(0, row[5])
                textbox.grid(row=2,column=1,padx=10,pady=10)

    def delete():
        category3 = category3_dropdown.get()
        subcategory3 = subcategory3_dropdown.get()

        with open("expenses.csv", 'r', newline='') as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)
            status = False
            for row in data:
                if len(row) >= 7:
                    if row[2]== user_id:
                        if row[3] == category3 and row[4] == subcategory3:
                            status = True
                            for i in range(0,7):
                                row[i] =''


        if status:
            with open("expenses.csv", 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data)
            message3_label.config(text="Entry Deleted")


        else:
            message1_label.config(text="Category or subcategory not found")


    category3_label = ttk.Label(frame3, text="Category:",background="yellow")
    category3_label.grid(row=0, column=0, padx=10, pady=10)

    category3_var = tkinter.StringVar()
    category3_dropdown = ttk.Combobox(frame3, textvariable=category3_var, values=list(categories.keys()),
                                      state="readonly")
    category3_dropdown.grid(row=0, column=1, padx=10, pady=10)

    subcategory3_label = ttk.Label(frame3, text="Subcategory:",background="yellow")
    subcategory3_label.grid(row=1, column=0, padx=10, pady=10)

    subcategory3_var = tkinter.StringVar()
    subcategory3_dropdown = ttk.Combobox(frame3, textvariable=subcategory3_var, state="readonly")
    subcategory3_dropdown.grid(row=1, column=1, padx=10, pady=10)

    def update_subcategories3(event):
        selected_category = category3_var.get()
        subcategories = categories[selected_category]
        subcategory3_dropdown.config(values=subcategories)

    category3_dropdown.bind("<<ComboboxSelected>>", update_subcategories3)

    show_button = ttk.Button(frame3, text="Show current amount", command=show_amount1)
    show_button.grid(row=2, column=0, padx=10, pady=10)

    delete_button = ttk.Button(frame3, text="Delete entry", command=delete)
    delete_button.grid(row=3, column=0, padx=10, pady=10)

    message3_label = ttk.Label(frame3, text="")
    message3_label.grid(row=4, column=0, padx=10, pady=10)
