import tkinter as tk
import tkinter.scrolledtext as tkst
from datetime import datetime
import sys,time,random

class Console:
    def __init__(self, root):
        # Creates a console field for displaying messages and errors.
        self.console = tkst.Text(root, height=17, width=55, fg="#fff", bg="#2e465e", font=("Calibri", 10),
                            borderwidth=1, relief="solid")
        #self.console.bind("<Key>", lambda e: "break")
        self.console.bind("<1>", lambda e: 'break')
        self.create_console()

    def create_console(self):
        # Placing cursor in the text area
        #self.console.focus()
        self.console.pack()
        self.console.place(x=6, y=220)

    def select_pictures(choice_pictures):
        print(choice_pictures)

    def select_videos(choice_videos):
        print(choice_videos)

    def slow_type(text):
        typing_speed = 300  # wpm
        for l in text:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(random.random() * 10.0 / typing_speed)
        print('')

    def greetings(self):
        return self.console.insert(tk.END, ("Welcome to Insta Media Pro. " \
               "\n\n1) Enter the username of the account you'd like to download." \
               "\n2) Select one or more media type to extract." \
               "\n3) Click on the download button below.\n" \
               "\nNote: In order to download media from a private account you must be\n"
                        "logged in and be a follower of the private account on Instagram.\n"))

    def print_text(self, text):
        return self.console.insert(tk.END, (datetime.now().strftime(
                '[%H:%M:%S]') + " " + str(text)))

    def clean_console(self):
        return self.console.delete(1.0, tk.END)