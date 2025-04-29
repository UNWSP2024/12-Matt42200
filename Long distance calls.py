import tkinter as tk
from tkinter import messagebox


rates = {
    "Daytime (6:00 AM - 5:59 PM)": 0.02,
    "Evening (6:00 PM - 11:59 PM)": 0.12,
    "Off-Peak (12:00 AM - 5:59 AM)": 0.05
}


def calculate_charge():
    try:
        minutes = float(minutes_entry.get())
        if minutes < 0:
            raise ValueError("Minutes must be non-negative.")
        rate = rates[rate_var.get()]
        charge = rate * minutes
        messagebox.showinfo("Call Charge", f"Total charge: ${charge:.2f}")
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")


root = tk.Tk()
root.title("Long-Distance Call Calculator")


rate_frame = tk.LabelFrame(root, text="Select Rate Category", padx=10, pady=10)
rate_frame.pack(padx=10, pady=10)


rate_var = tk.StringVar()
rate_var.set("Daytime (6:00 AM - 5:59 PM)")  # default selection


for rate_label in rates.keys():
    tk.Radiobutton(rate_frame, text=rate_label, variable=rate_var, value=rate_label).pack(anchor='w')


tk.Label(root, text="Enter call duration (minutes):").pack()
minutes_entry = tk.Entry(root)
minutes_entry.pack(pady=5)


tk.Button(root, text="Calculate Charge", command=calculate_charge).pack(pady=10)




root.mainloop()