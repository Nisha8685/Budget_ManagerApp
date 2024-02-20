import tkinter
from tkinter import ttk
from tkinter import messagebox
import csv
from openpyxl import Workbook


def reports(user_id):
    filename = 'expenses.csv'
    categories = {}

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            if len(row) >= 7 and row[2] == user_id:
                category = row[3]
                subcategory = row[4]
                amount = float(row[5])
                date = row[6]


                if category not in categories:
                    categories[category] = []
                categories[category].append((subcategory, amount, date))

    # Create a new Excel workbook
    wb = Workbook()
    ws = wb.active

    # Write data to the Excel worksheet
    ws.append(["Category", "Subcategory", "Amount", "Date"])
    for category, items in categories.items():
        for subcategory, amount, date in items:
            ws.append([category, subcategory, amount, date])

    # Save the Excel workbook
    wb.save("expense_report.xlsx")