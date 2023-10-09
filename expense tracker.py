#expense tracker 

import tkinter as tk
from tkinter import messagebox

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        # Variables
        self.expense_list = []

        # GUI Components
        self.label = tk.Label(root, text="Enter Expense:")
        self.label.pack(pady=10)

        self.expense_entry = tk.Entry(root)
        self.expense_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.pack(pady=10)

        self.show_button = tk.Button(root, text="Show Expenses", command=self.show_expenses)
        self.show_button.pack(pady=10)

    def add_expense(self):
        expense = self.expense_entry.get()
        if expense:
            self.expense_list.append(expense)
            messagebox.showinfo("Expense Tracker", f"Expense '{expense}' added successfully.")
            self.expense_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Expense Tracker", "Please enter a valid expense.")

    def show_expenses(self):
        if not self.expense_list:
            messagebox.showinfo("Expense Tracker", "No expenses to show.")
        else:
            expenses_text = "\n".join(self.expense_list)
            messagebox.showinfo("Expense Tracker", f"Expenses:\n{expenses_text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()