import sqlite3

# Connect to database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    amount REAL,
    description TEXT
)
""")

conn.commit()


# Add expense
def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    cursor.execute(
        "INSERT INTO expenses (category, amount, description) VALUES (?, ?, ?)",
        (category, amount, description)
    )
    conn.commit()
    print("Expense added successfully!\n")


# View expenses
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    print("\n--- All Expenses ---")
    for row in rows:
        print(f"ID: {row[0]} | Category: {row[1]} | Amount: €{row[2]} | Note: {row[3]}")
    print()


# Total spent
def total_spent():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print(f"\nTotal Spent: €{total}\n")


# Main menu
while True:
    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spent")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_spent()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.\n")

conn.close()
