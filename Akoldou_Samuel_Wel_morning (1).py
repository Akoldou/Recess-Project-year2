import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ReceiptItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Receipt:
    def __init__(self, customer_name, receipt_items, tax_rate):
        self.customer_name = customer_name
        self.receipt_items = receipt_items
        self.tax_rate = tax_rate

    def calculate_total_cost(self):
        total_cost = sum(item.price for item in self.receipt_items)
        return total_cost

    def calculate_tax_amount(self):
        total_cost = self.calculate_total_cost()
        tax_amount = total_cost * (self.tax_rate / 100)
        return tax_amount

    def generate_receipt_text(self):
        total_cost = self.calculate_total_cost()
        tax_amount = self.calculate_tax_amount()
        grand_total = total_cost + tax_amount

        receipt_text = f"Customer: {self.customer_name}\n"

        for item in self.receipt_items:
            receipt_text += f"{item.name}: ${item.price:.2f}\n"

        receipt_text += f"Total cost: ${total_cost:.2f}\n"
        receipt_text += f"Tax rate: {self.tax_rate}%\n"
        receipt_text += f"Tax amount: ${tax_amount:.2f}\n"
        receipt_text += f"Grand total: ${grand_total:.2f}\n"
        receipt_text += f"Date: {datetime.now():%Y-%m-%d}\n"
        receipt_text += f"Time: {datetime.now():%H:%M:%S}\n"

        return receipt_text

def print_receipt():
    try:
        # Get the values from the entry fields
        customer_name = name_entry.get()
        tax_rate = float(tax_rate_entry.get())

        receipt_items = []
        for i in range(len(item_entries)):
            item_name = item_entries[i].get()
            item_price = float(price_entries[i].get())
            receipt_items.append(ReceiptItem(item_name, item_price))

        # Create a Receipt object
        receipt = Receipt(customer_name, receipt_items, tax_rate)

        # Generate the receipt text
        receipt_text = receipt.generate_receipt_text()

        # Append "Thank you" message
        receipt_text += "Thank you for shopping with us!\n"

        # Create a new window for the receipt
        receipt_window = tk.Toplevel(root)
        receipt_window.title("Receipt")

        # Create a text widget to display the receipt
        receipt_text_widget = tk.Text(receipt_window, font=("Courier", 12))
        receipt_text_widget.insert(tk.END, receipt_text)
        receipt_text_widget.configure(state="disabled")
        receipt_text_widget.pack()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid data for all fields.")

def clear():
    # Clear all entry fields
    name_entry.delete(0, tk.END)
    tax_rate_entry.delete(0, tk.END)

    for entry in item_entries:
        entry.delete(0, tk.END)

    for entry in price_entries:
        entry.delete(0, tk.END)

    # Set focus to the first entry field
    name_entry.focus_set()

# Create the main window
root = tk.Tk()
root.title("Receipt Printing Program")

# Create labels and entry fields for customer details
name_label = tk.Label(root, text="Customer Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Create labels and entry fields for item details
item_labels = []
item_entries = []
price_labels = []
price_entries = []

for i in range(5):
    item_label = tk.Label(root, text=f"Item {i+1} Name:")
    item_label.pack()
    item_entry = tk.Entry(root)
    item_entry.pack()
    item_labels.append(item_label)
    item_entries.append(item_entry)

    price_label = tk.Label(root, text=f"Item {i+1} Price:")
    price_label.pack()
    price_entry = tk.Entry(root)
    price_entry.pack()
    price_labels.append(price_label)
    price_entries.append(price_entry)

tax_rate_label = tk.Label(root, text="Tax Rate (%):")
tax_rate_label.pack()
tax_rate_entry = tk.Entry(root)
tax_rate_entry.pack()

# Create buttons for printing and clearing
button_frame = tk.Frame(root)
button_frame.pack()

print_button = tk.Button(button_frame, text="Print Receipt", command=print_receipt)
print_button.pack(side=tk.LEFT)

clear_button = tk.Button(button_frame, text="Clear", command=clear)
clear_button.pack(side=tk.LEFT)

exit_button = tk.Button(button_frame, text="Exit", command=root.destroy)
exit_button.pack(side=tk.LEFT)

# Start the main event loop
root.mainloop()



