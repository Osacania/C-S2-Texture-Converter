import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import settings

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("C:S2 Texture Converter")
        
        #メニューバー
        menubar = tk.Menu(self.master)
        root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        
        file_menu.add_command(label="Preferances", command=self.open_preferance)
        
        #操作フォルダ選択部分
        frame1 = ttk.Frame(self.master, padding="10")
        frame1.grid(row=0, column=0, sticky=(tk.NSEW))
        
        self.path_entry = ttk.Entry(frame1)
        self.path_entry.grid(row=0, column=0, pady=5)
        
        button1 = ttk.Button(frame1, text="Browse", command=self.open_filedialog)
        button1.grid(row=0, column=1, pady=5)
        
        frame2 = ttk.Frame(self.master, padding="10")
        frame2.grid(row=1, column=0, sticky=(tk.NSEW))
        
        v1 = tk.BooleanVar(value = False)
        checkbtn = ttk.Checkbutton(
            frame2, text="Check!",
            variable= v1)
        checkbtn.grid(row=0, column=0, pady=5)
        
    def open_filedialog(self):
        dir = settings.DEFAULT_DIR
        fld = filedialog.askdirectory(initialdir = dir)
        self.path_entry.delete(0, tk.END) #入力欄にパスを表示する
        self.path_entry.insert(0, fld)
        settings.DEFAULT_DIR = fld #次回同じフォルダを表示するために記録する
        
    def open_preferance(self):
        dlg_preferance = tk.Toplevel(self)
        dlg_preferance.title("Preferances")
        
        frame1 = ttk.Frame(dlg_preferance, padding="10")
        frame1.grid(row=0, column=0, sticky=(tk.NSEW))
        
        language_label = ttk.Label(frame1, text="Language")
        language_label.grid(row=0, column=0, pady=5)
        
        lang_list = ["English", "Japanese"]
        language_select = ttk.Combobox(frame1, values=lang_list)
        language_select.grid(row=0, column=1, pady=5)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
