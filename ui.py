from tkinter import *
from tkinter import ttk

root = Tk()

frame = ttk.Frame(root, padding=10)
frame.grid()

# Unit textbox
ttk.Label(frame, text="Unit: ").grid(column=0, row=0, sticky = W, pady = 2)
unit= ""
ttk.Entry(frame, textvariable = unit).grid(column = 1, row = 0)

# Encode textbox
ttk.Label(frame, text = "Encode: ").grid(column = 0, row = 1, sticky = W, pady = 2)
encode = ""
ttk.Entry(frame, textvariable = encode).grid(column = 1, row = 1)

ttk.Button(frame, text = "Generate Barcode").grid(row = 2, column = 0, sticky = W, columnspan = 4)
