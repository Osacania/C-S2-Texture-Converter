import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import settings

def open_filedialog():
    dir = settings.DEFAULT_DIR
    fld = filedialog.askdirectory(initialdir = dir)
    path_entry.delete(0, tk.END)
    path_entry.insert(0, fld)
    settings.DEFAULT_DIR = fld

root = tk.Tk()
root.title("C:S2 Texture Converter")

#操作フォルダ選択部分
frame1 = ttk.Frame(root, padding="10")
frame1.grid(row=0, column=0, sticky=(tk.NSEW))

path_entry = ttk.Entry(frame1)
path_entry.grid(row=0, column=0, pady=5)

button1 = ttk.Button(frame1, text="Browse", command=open_filedialog)
button1.grid(row=0, column=1, pady=5)

frame2 = ttk.Frame(root, padding="10")
frame2.grid(row=1, column=0, sticky=(tk.NSEW))

v1 = tk.BooleanVar(value = False)
checkbtn = ttk.Checkbutton(
    frame2, text="Check!",
    variable= v1)
checkbtn.grid(row=0, column=0, pady=5)

root.mainloop()