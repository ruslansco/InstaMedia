import tkinter as tk
import tkinter.scrolledtext as tkst
import main


class Console:

    def __init__(self, root):
        # Creates a console field for displaying messages and errors.
        self.console = tkst.Text(root, height=14, width=48, fg="#fff", bg="#2e465e", font=("Comic Sans MS", 10),
                            borderwidth=1, relief="solid")
        self.console.bind("<Key>", lambda e: "break")
        self.create_console()

    def create_console(self):
        # Placing cursor in the text area
        self.console.focus()
        self.console.pack()
        self.console.place(x=7, y=260)

    def select_pictures(choice_pictures):
        print(choice_pictures)

    def select_videos(choice_videos):
        print(choice_videos)

    def greetings(self):
        return "Welcome to Insta Media Pro. " \
               "\n\n1) Type in an instagram username above (ex: @username). " \
               "\n2) Choose a type of account. " \
               "\n3) Select media to download." \
               "\n4) Click on download button below.\n" \
               "\n Note: In order to exctract media from private you will have to login to your instagram."