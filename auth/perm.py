import instaloader


class setPermissions():

    def pass_values(images_p, videos_p):
        """
        """
        bot = instaloader.Instaloader(
            download_pictures=images_p,
            download_videos=videos_p,
            download_video_thumbnails=False,
            compress_json=False,
            download_geotags=False,
            post_metadata_txt_pattern=None,
            max_connection_attempts=0,
            download_comments=False, )
        #print("Values: " + images_p + " and " + videos_p + "have been passed to bot.")
        return bot
