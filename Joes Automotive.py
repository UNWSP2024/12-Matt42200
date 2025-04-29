import tkinter as tk
from tkinter import messagebox


services = {
    "Oil Change": 30.0,
    "Lube Job": 20.0,
    "Radiator Flush": 40.0,
    "Transmission Fluid": 100.0,
    "Inspection": 35.0,
    "Muffler Replacement": 200.0,
    "Tire Rotation": 20.0
}


def calculate_total():
    total = 0
    for service, var in check_vars.items():
        if var.get():
            total += services[service]
    total_label.config(text=f"Total Charges: ${total:.2f}")


root = tk.Tk()
root.title("Joe's Automotive Services")


frame = tk.Frame(root, padx=10, pady=10)
frame.pack()


check_vars = {}
row = 0
for service, price in services.items():
    var = tk.BooleanVar()
    check_vars[service] = var
    cb = tk.Checkbutton(frame, text=f"{service} - ${price:.2