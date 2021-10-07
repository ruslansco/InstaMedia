from tkinter import *
import tkinter as tk
from tkinter import ttk
import main

class loadingWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.progress = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        self.progress.pack(fill=BOTH, expand=1)
        self.val = 0
        self.maxval = 1
        self.progress["maximum"] = 1


    def updating(self, val):
        self.val = val
        self.progress["value"] = self.val
        app.title("Loading " + str(int(self.val * 100)) + "%")
        if self.val == self.maxval:
            self.destroy()

    def test(self,i=0):
        app.updating(i / 50)
        if i < 100:
            app.after(50, self.test, i + 1)

if __name__ == '__main__':
    app = loadingWindow()
    app.after(1, app.test)
    app.geometry("250x20+650+350")
    app.title("Authenticating")
    app.wm_attributes("-alpha", "0.99")
    app.overrideredirect(True)
    # Always keep window on top of others
    app.attributes('-topmost', True)
    # Fixed size
    app.resizable(width=False, height=False)
    app.mainloop()