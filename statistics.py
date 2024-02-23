import tkinter
import tkinter.messagebox
from tkinter import ttk
from tkinter import messagebox
import csv
import matplotlib
from matplotlib import pyplot as plt
def statistics(user_id):

    def extract(filename):
        categories = {}  # Dictionary to store category/subcategory totals
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                if len(row) >= 7:  # Ensure row has enough elements
                    if row[2]==user_id:
                        category = row[3]  # Field 3: Category
                        subcategory = row[4]  # Field 5: Subcategory
                        amount = float(row[5])  # Field 6: Amount
                        # Update category/subcategory totals
                        if category in categories:
                            categories[category][subcategory] = categories[category].get(subcategory, 0) + amount
                        else:
                            categories[category] = {subcategory: amount}
        return categories

    # Function to create and display the pie chart
    def create_pie_chart(categories):
        labels = []  # Labels for the pie chart
        sizes = []  # Sizes (amounts) for the pie chart
        for category, subcategories in categories.items():
            for subcategory, amount in subcategories.items():
                labels.append(category + ' - ' + subcategory)
                sizes.append(amount)
        plt.figure(figsize=(8, 8))  # Set the size of the pie chart
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Expense Distribution')
        plt.show()

    categories=extract("expenses.csv")
    create_pie_chart(categories)
