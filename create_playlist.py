"""
Step 1: Log into YouTube
Step 2: Get Liked Videos
Step 3: Create a new Playlist in Spotify
Step 4: Search for the song
Step 5: Add this song to the new Spotify Playlist
"""
import json
from secrets import spotify_user_id
class CreatePlaylist:

    def __int__(self):
        self.user_id = spotify_user_id

    #Step 1: Log into YouTube
    def get_youtube_client(self):
        pass

    #Step 2: Get our liked videos
    def get_liked_videos(self):
        pass

    #Step 3: Create a new Playlist
    def create_playlist(self):
        request_body = json.dumps({
            "name":"YouTube Liked Playlist",
            "description": "All Liked YouTube Videos",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{user_id}/playlists".format(self.user_id)


    #Step 4: Search for the song
    def get_spotify_url(self):
        pass

    #Step 5: Add song to the new Spotify Playlist
    def add_song_to_playlist(self):
        pass
