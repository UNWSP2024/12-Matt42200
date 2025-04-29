import tkinter as tk
from tkinter import messagebox


def calculate_mpg():
    try:
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())
        if gallons <= 0:
            raise ValueError("Gallons must be greater than zero.")
        mpg = miles / gallons
        result_label.config(text=f"Miles Per Gallon (MPG): {mpg:.2f}")
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")


root = tk.Tk()
root.title("Gas Mileage Calculator")


tk.Label(root, text="Gallons of Gas:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
gallons_entry = tk.Entry(root)
gallons_entry.grid(row=0, column=1, padx=10, pady=5)


tk.Label(root, text="Miles on Full Tank:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
miles_entry = tk.Entry(root)
miles_entry.grid(row=1, column=1, padx=10, pady=5)


calc_button = tk.Button(root, text="Calculate MPG", command=calculate_mpg)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)


result_label = tk.Label(root, text="Miles Per Gallon (MPG):", font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=10)


root.mainloop()