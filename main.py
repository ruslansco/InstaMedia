#!/usr/bin/python3
# InstaMedia
# version 0.1.0
# https://github.com/ruslansco/InstaMedia
# Start Date: 05/10/2021
# Rev Date: 10/07/2021


import tkinter as tk
import instaloader
from datetime import datetime
import terminal
import auth
from pathlib import Path, PureWindowsPath
import os
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk
import sys

class Root(tk.Frame):
    """Class creates an interface."""

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.create_root()
        self.create_navbar()
        self.create_entry()
        self.create_check_buttons()
        self.create_start_button()
        self.run_console()

    def create_root(self):
        panel = tk.Label(root, bg="#15202b", borderwidth=1, relief="solid")
        panel.pack(side="bottom", fill="both", expand=1)
        root.title("Insta-Media-Pro")  # Title
        root.geometry("400x670+0+0")  # Size
        # Gets requested values of height and width.
        width = root.winfo_reqwidth()
        height = root.winfo_reqheight()
        # Gets both screen width/height and window width/height
        position_right = int(root.winfo_screenwidth() / 3 - width/ 3)
        position_down = int(root.winfo_screenheight() / 3 - height / 3)
        # Positions main window frame in the center of screen.
        root.geometry("+{}+{}".format(position_right,position_down))
        # Window Opacity 0.0-1.0
        root.wm_attributes("-alpha", "0.99")

        def savelastclick_position(event):
            global lastclick_x, lastclick_y
            lastclick_x = event.x
            lastclick_y = event.y
        def dragging(event):
            x, y = event.x - lastclick_x + root.winfo_x(), event.y - lastclick_y + root.winfo_y()
            root.geometry("+%s+%s" % (x, y))

        root.overrideredirect(True)
        # Always keep window on top of others
        root.attributes('-topmost', True)
        root.bind('<Button-1>', savelastclick_position)
        root.bind('<B1-Motion>', dragging)
        # Fixed size
        root.resizable(width=False, height=False)

    def create_navbar(self):
        """Creates logo in the root window."""
        # Header Title
        header_title = tk.Label(root, font=("Comic Sans MS", 22, "bold"), text="InstaMedia Pro", fg="#fff", bg="#000",
                             borderwidth=1, relief="solid")
        header_title.pack(fill=tk.BOTH)
        # Quit Button
        quit_icon = ImageTk.PhotoImage(file='icons/quit.jpg')
        quit_icon_button = Button(header_title, image=quit_icon, bg="#000", relief=FLAT,
                                  command=lambda: self.close_program())
        quit_icon_button.image = quit_icon
        quit_icon_button.place(x=340, y=0)

    def create_entry(self):
        global acc_input
        #target_account = tk.IntVar()
        """Creates fields in the root window"""
        # Title - "Instagram Account".
        acc_title = tk.Label(root, text="Enter Instagram Username", font=("Comic Sans MS", 15, "bold"), fg="#fff",
                          bg="#15202B")
        acc_title.pack()
        acc_title.place(x=55, y=55)

        # Input field for a target account.
        """
        def validate_input(in_str):
            if len(in_str) == 0:
                # empty Entry is ok
                return True
            elif len(in_str) == 30:
                # Entry with 1 digit is ok
                return True
            else:
                # Anything else, reject it
                return False
                """

        acc_input = tk.Entry(root, bd=1, fg="#fff", bg="#2e465e", font=("Arial", 12),
                                 borderwidth=1, relief="solid", validate="key")
        #acc_input['validatecommand'] = (acc_input.register(validate_input),'%S', '%d')

        acc_input.pack()
        acc_input.place(x=90, y=100)
        #acc_input.insert(tk.END,"@")
        acc_input.focus_set()  # Set cursor focus to the entry.



    def create_check_buttons(self):
        """Creates 3 check-buttons in root window for downloading media: Pictures, Videos, Stories."""

        choice_pictures = tk.IntVar()
        choice_videos = tk.IntVar()

        # Title - "Select Media"
        media_title = tk.Label(root, text="Select Media Type", font=("Comic Sans MS", 13, 'bold'),
                               fg="#fff", bg="#15202B")
        media_title.pack()
        media_title.place(x=100, y=135)

        # Checkbutton1 - "Pictures"
        media_pictures = tk.Checkbutton(root, text="Pictures", fg="#2e465e", bg="#15202B",
                                        font=("Comic Sans MS", 13), variable=choice_pictures)
        media_pictures.pack()
        media_pictures.place(x=30, y=165)

        # Checkbutton2 - "Videos"
        media_video = tk.Checkbutton(root, text="Videos", fg="#2e465e", bg="#15202B",
                                     font=("Comic Sans MS", 13), variable=choice_videos)
        media_video.pack()
        media_video.place(x=150, y=165)

        # Checkbutton3 - "Stories"
        media_stories = tk.Checkbutton(root, text="Stories", fg="#2e465e", bg="#15202B",
                                       font=("Comic Sans MS", 13))
        media_stories.pack()
        media_stories.place(x=270, y=165)

    def create_start_button(self):
        """Creates a start button inside the root window."""
        # Start(download) button
        start_icon = tk.PhotoImage(file='../InstaMedia/icons/start.png')
        start_icon_button = tk.Button(root, image=start_icon, bg="#15202B", height="125", width="125",
                                      relief=tk.FLAT, command=lambda: Root.press_start_button(self, acc_input.get()))
        start_icon_button.image = start_icon
        start_icon_button.place(x=132, y=530)

    def run_console(self):
        global run
        run = terminal.Console(root)
        run.greetings()

    def press_start_button(self, target_username):
        target_username = self.is_target_valid(target_username)

    def is_target_valid(self, target_value):
        for retry in range(1):
            if len(target_value) >= 3:
                run.clean_console()
                run.print_text("(Message) Analyzing username: '"+target_value+"'...")
            else:
                acc_input.delete(tk.END)
                run.clean_console()
                run.print_text(
                    "(Error): Target Instagram username field cannot be empty or less than 3 characters. Type in the username of the account you'd like to download in the field above.. Ex:@ruslansco\n")
                break
        return None

    # function to call when user press
    # the save button, a filedialog will
    # open and ask to save file
    #def request_directory(self):
    #    root.withdraw()
    #    folder_selected = filedialog.askdirectory()
    #    return folder_selected

    def close_program(self):
        root.destroy()

    def disable_event(self):
        pass

if __name__ == '__main__':
    root = tk.Tk()
    app = Root(root)
    root.mainloop()


