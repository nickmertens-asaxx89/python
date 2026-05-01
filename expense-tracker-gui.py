import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# -------------------------
# DATABASE
# -------------------------
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    note TEXT,
    date TEXT
)
""")
conn.commit()


# -------------------------
# FUNCTIONS
# -------------------------
def add_expense():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        note = note_entry.get()
        date = datetime.now().strftime("%Y-%m-%d")

        cursor.execute("""
            INSERT INTO expenses(amount, category, note, date)
            VALUES (?, ?, ?, ?)
        """, (amount, category, note, date))

        conn.commit()
        refresh_table()

        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        note_entry.delete(0, tk.END)

    except:
        messagebox.showerror("Error", "Invalid input")


def refresh_table():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)

    show_total()


def delete_expense():
    selected = tree.selection()

    if not selected:
        return

    item = tree.item(selected[0])
    expense_id = item["values"][0]

    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()

    refresh_table()


def show_total():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    total_label.config(text=f"Total Spent: €{total}")


# -------------------------
# GUI
# -------------------------
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("800x600")

# Form
tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Note").pack()
note_entry = tk.Entry(root)
note_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)

# Table
columns = ("ID", "Amount", "Category", "Note", "Date")

tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)

tree.pack(fill="both", expand=True)

# Buttons
tk.Button(root, text="Delete Selected", command=delete_expense).pack(pady=10)

total_label = tk.Label(root, text="Total Spent: €0", font=("Arial", 14))
total_label.pack()

refresh_table()

root.mainloop()