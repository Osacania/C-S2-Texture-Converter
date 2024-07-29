import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import configparser
import os
import glob
#あとで実装する
#import gettext
from settings import LANGUAGES, SETTINGS_FILE
from image_process import conbine_image

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        #i18n関連はうまくいかなかったので後で実装する
        #path_to_locale_dir = os.path.abspath(
        #    os.path.join(
        #        os.path.dirname(__file__), 
        #        "locale"
        #    )
        #)
        
        #translater = gettext.translation(
        #    "messages",
        #    localedir=path_to_locale_dir,
        #    languages=["en_US"],
        #    fallback=True
        #)
        
        #translater.install()
        
        self.master.title("C:S2 Texture Converter")
        
        #メニューバー
        menubar = tk.Menu(self.master)
        root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='ファイル', menu=file_menu)
        
        file_menu.add_command(label='環境設定', command=self.open_preferance_modeless)
        
        #操作フォルダ選択部分
        frame1 = ttk.Frame(self.master, padding="10")
        frame1.grid(row=0, column=0, sticky=(tk.NSEW))
        
        path_label = ttk.Label(frame1, text="ファイルパス", anchor=tk.W)
        path_label.grid(row=0, column=0)
        
        self.path_entry = ttk.Entry(frame1)
        self.path_entry.grid(row=1, column=0, pady=5)
        
        button1 = ttk.Button(frame1, text='参照', command=self.open_filedialog)
        button1.grid(row=1, column=1, pady=5)
        
        frame2 = ttk.Frame(self.master, padding="10")
        frame2.grid(row=1, column=0, sticky=(tk.NSEW))
        
        path_filename = ttk.Label(frame2, text="ファイル名(_より前のみ)", anchor=tk.W)
        path_filename.grid(row=0, column=0)
               
        self.filename_entry = ttk.Entry(frame2)
        self.filename_entry.grid(row=1, column=0, pady=5)
        
        button2 = ttk.Button(frame2, text="画像合成", command=self.process_image)
        button2.grid(row=1, column=1, pady=5)
        
    def open_filedialog(self):
        dir = self.load_settings("Settings", "directory")
        fld = filedialog.askdirectory(initialdir = dir)
        if fld:
            self.path_entry.delete(0, tk.END) #入力欄にパスを表示する
            self.path_entry.insert(0, fld)
            self.save_settings("Settings", "directory", fld) #次回同じフォルダを表示するために記録する
        
    def open_preferance_modeless(self):
        dlg_preferance = tk.Toplevel(self)
        dlg_preferance.title("Preferances")
        
        frame1 = ttk.Frame(dlg_preferance, padding="10")
        frame1.grid(row=0, column=0, sticky=(tk.NSEW))
        
        language_label = ttk.Label(frame1, text="言語（WIP）")
        language_label.grid(row=0, column=0, pady=5)
        #言語選択欄
        language_names = [lang["name"] for lang in LANGUAGES]
        language_select = ttk.Combobox(frame1, values=language_names, state="readonly")
        language_select.grid(row=0, column=1, pady=5)
        
    def save_settings(self, section, option, value):
        if os.path.exists(SETTINGS_FILE):
            config = configparser.ConfigParser()
            config.read(SETTINGS_FILE)
            config.set(section, option, value)
            
    def load_settings(self, section, option):
        if os.path.exists(SETTINGS_FILE):
            config = configparser.ConfigParser()
            config.read(SETTINGS_FILE)
            value = config.get(section, option)
        return value
    
    def process_image(self):
        path = self.path_entry.get() + "/"
        filename = self.filename_entry.get()
        
        conbine_image(path, filename)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()