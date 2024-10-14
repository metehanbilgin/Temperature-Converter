import tkinter as tk
from tkinter import ttk

def convert_temperature():
    temp = float(entry_temp.get())
    if selected_unit.get() == "Celsius to Fahrenheit":
        converted_temp = (temp * 9/5) + 32
        result_label.config(text=f"{converted_temp:.2f} °F")
    else:
        converted_temp = (temp - 32) * 5/9
        result_label.config(text=f"{converted_temp:.2f} °C")


window = tk.Tk()
window.title("Temperature Converter")


window_width = 300
window_height = 200

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int((screen_width - window_width) / 2)
center_y = int((screen_height - window_height) / 2)

window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

entry_temp = ttk.Entry(window, width=15)
entry_temp.grid(column=1, row=0, padx=10, pady=10)

selected_unit = tk.StringVar()
unit_combobox = ttk.Combobox(window, textvariable=selected_unit, width=20, state="readonly")
unit_combobox['values'] = ("Celsius to Fahrenheit", "Fahrenheit to Celsius")
unit_combobox.grid(column=1, row=1, padx=10, pady=10)
unit_combobox.current(0)

convert_button = ttk.Button(window, text="Convert", command=convert_temperature)
convert_button.grid(column=1, row=2, padx=10, pady=10)

result_label = ttk.Label(window, text="Result", font=("Arial", 12), background="#f0f0f0", foreground="#ff0000")
result_label.grid(column=1, row=3, padx=10, pady=10)

ttk.Label(window, text="Temperature:").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(window, text="Conversion:").grid(column=0, row=1, padx=10, pady=10)

window.mainloop()
