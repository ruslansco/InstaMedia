#!/usr/bin/python3
# InstaMedia
# version 0.0.3
# https://github.com/ruslansco/InstaMedia
# Start Date: 05/10/2021
# Rev Date: 07/07/2021


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

class Root(tk.Frame):
    """Class creates an interface."""

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.create_root()
        self.create_navbar()
        self.create_entry()
        self.create_radio_buttons()
        self.run_console()
        self.create_check_buttons()
        self.create_start_button()

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
        header_title = tk.Label(root, font=("Comic Sans MS", 22, "bold"), text="Insta Media Pro", fg="#fff", bg="#000",
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
        target_account = tk.IntVar()
        """Creates fields in the root window"""
        # Title - "Instagram Account".
        acc_title = tk.Label(root, text="Target Instagram Account", font=("Comic Sans MS", 15, "bold"), fg="#fff",
                          bg="#15202B")
        acc_title.pack()
        acc_title.place(x=55, y=55)

        # Input field for a target account.
        acc_input = tk.Entry(root, bd=1, fg="#fff", bg="#2e465e", font=("Arial", 12),
                             borderwidth=1, relief="solid")
        acc_input.pack()
        acc_input.place(x=90, y=100)
        acc_input.insert(tk.END,"@")
        acc_input.focus_set()  # Set cursor focus to the entry.

    def create_radio_buttons(self):
        """Creates 2 radio-buttons in root window to determine type of account: Public or Private"""
        # Radiobutton1 - "Public"
        acc_public = tk.Radiobutton(root, text="Public", font=("Comic Sans MS", 13),
                                 fg="#2e465e", bg="#15202B", value=1)
        acc_public.pack()
        acc_public.place(x=80, y=130)

        # Radiobutton2 - "Private"
        acc_private = tk.Radiobutton(root, text="Private", font=("Comic Sans MS", 13),
                                  fg="#2e465e", bg="#15202B", value=2)
        acc_private.pack()
        acc_private.place(x=180, y=130)

    def create_check_buttons(self):
        """Creates 3 check-buttons in root window for downloading media: Pictures, Videos, Stories."""

        choice_pictures = tk.IntVar()
        choice_videos = tk.IntVar()

        # Title - "Select Media"
        media_title = tk.Label(root, text="Select Media Type", font=("Comic Sans MS", 14, 'bold'),
                               fg="#fff", bg="#15202B")
        media_title.pack()
        media_title.place(x=90, y=180)

        # Checkbutton1 - "Pictures"
        media_pictures = tk.Checkbutton(root, text="Pictures", fg="#2e465e", bg="#15202B",
                                        font=("Comic Sans MS", 13), variable=choice_pictures)
        media_pictures.pack()
        media_pictures.place(x=30, y=220)

        # Checkbutton2 - "Videos"
        media_video = tk.Checkbutton(root, text="Videos", fg="#2e465e", bg="#15202B",
                                     font=("Comic Sans MS", 13), variable=choice_videos)
        media_video.pack()
        media_video.place(x=150, y=220)

        # Checkbutton3 - "Stories"
        media_stories = tk.Checkbutton(root, text="Stories", fg="#2e465e", bg="#15202B",
                                       font=("Comic Sans MS", 13))
        media_stories.pack()
        media_stories.place(x=270, y=220)

    def create_start_button(self):
        """Creates a start button inside the root window."""
        # Start(download) button
        start_icon = tk.PhotoImage(file='../InstaMedia/icons/start.png')
        start_icon_button = tk.Button(root, image=start_icon, bg="#15202B", height="125", width="125",
                                      relief=tk.FLAT, command=lambda: self.open_login_window())
        start_icon_button.image = start_icon
        start_icon_button.place(x=132, y=530)

    def run_console(self):
        global run
        run = terminal.Console(root)
        run.console.insert(tk.END,run.greetings())

    def open_login_window(self):
        """Method opens a login window and """

        login_window = tk.Tk()
        login_window.geometry("250x100")  # Login window size.
        login_window.title("Login to Instagram")  # Login window title.

        def login(event=None):
            """Creates an instance of User class from auth.py"""
            run.console.delete(1.0, tk.END)
            run.console.insert(tk.END, datetime.now().strftime(
                '(%H:%M:%S)') + " [Message]: Attempting to authenticate...\n")
            user = auth.User(a.get(), b.get())
            user.set_permissions(True, False)

            try:
                auth.bot.login(user.username, user.password)  # Load session and attempt to login.
                run.console.insert(tk.END, datetime.now().strftime(
                '(%H:%M:%S)') + " [Success]: Account @" + user.username + " has been found.\n")
                run.console.insert(tk.END, datetime.now().strftime(
                '(%H:%M:%S)') + " [Success]: Successfully logged in via " + user.username + ".\n\n")
                login_window.destroy()
                # Obtain profile metadata
                profile = instaloader.Profile.from_username(auth.bot.context,acc_input.get())

                # Get all video-posts in a generator object
                posts = profile.get_posts()
                directory = self.request_directory()
                # Iterate and download videos from profile
                for index, post in enumerate(posts, 1):
                    file = auth.bot.download_post(post, target=Path(directory))

            except instaloader.InvalidArgumentException:
                run.console.insert(tk.END, datetime.now().strftime(
                    '(%H:%M:%S)') + " [Error]: Account @" + user.username + " does not exist.\n\n")
            except instaloader.BadCredentialsException:
                run.console.insert(tk.END, datetime.now().strftime(
                '(%H:%M:%S)') + " [Success]: Account @" + user.username + " has been found.\n")
                run.console.insert(tk.END,datetime.now().strftime(
                '(%H:%M:%S)') + " [Error]: Wrong password. Please try again.\n\n")
            except instaloader.ConnectionException:
                run.console.insert(tk.END, datetime.now().strftime(
                '(%H:%M:%S)') + " [Error]: Please wait a few minutes before you try again.\n\n")

        # Fields for username and password.
        tk.Label(login_window, text="Username").grid(row=0, column=0)
        tk.Label(login_window, text="Password").grid(row=1, column=0)
        a = tk.Entry(login_window)
        b = tk.Entry(login_window, show="*")
        a.grid(row=0, column=1, sticky="e")  # Place username and password.
        a.focus_set()  # Set cursor focus to username.
        b.grid(row=1, column=1, sticky="e")
        # Keep me signed in checkbox.
        checkbox = tk.Checkbutton(login_window, text="Keep me logged in")
        checkbox.grid(row=2, column=1)
        # Login Button
        loginbutton = tk.Button(login_window, text="Login", command=lambda: login())
        loginbutton.grid(row=3, column=1)
        # Click button by pressing enter key.
        loginbutton.bind('<Return>', login)
        login_window.mainloop()

    # function to call when user press
    # the save button, a filedialog will
    # open and ask to save file
    def request_directory(self):
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        return folder_selected

    def close_program(self):
        root.destroy()

    def disable_event(self):
        pass

if __name__ == '__main__':
    root = tk.Tk()
    app = Root(root)
    root.mainloop()