import instaloader
import tkinter as tk
import main

class User:
    """Authenticates a user in instagram."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def set_permissions(self, download_pictures, download_videos):
        """
        Method is used to login with given credentials from users input(main.Main.login(self)).
        If username and password correct, login windows gets destroyed.
        If username or password incorrect, login window reappear (up to 500 attempts).
        """
        global bot
        bot = instaloader.Instaloader(
            download_pictures,
            download_videos,
            download_video_thumbnails=False,
            compress_json=False,
            download_geotags=False,
            post_metadata_txt_pattern=None,
            max_connection_attempts=0,
            download_comments=False, )
        return bot