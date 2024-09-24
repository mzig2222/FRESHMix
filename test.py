import praw
import spotipy
import spotipy.util
from spotipy.oauth2 import SpotifyOAuth

def sp_Authenticate(username):
    scope = "playlist-modify-public"
    token = spotipy.util.prompt_for_user_token(
        username=username, 
        scope="playlist-modify-public user-top-read",
        client_id="",
        client_secret="",
        redirect_uri="https://example.com/callback"
    )
    return token

r = praw.Reddit(client_id = "",
                client_secret = "",
                username = "*********",
                password = "***********",
                user_agent = "freshMixv1")

username='mzig22222'
s = spotipy.Spotify(sp_Authenticate(username))

a = s.album('https://open.spotify.com/album/4GNIhgEGXzWGAefgN5qjdU')

for track in a['tracks']['items']:
    print(track['id'])
