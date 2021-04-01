import praw
import spotipy
import spotipy.util
from spotipy.oauth2 import SpotifyOAuth

def sp_Authenticate(username):
    scope = "playlist-modify-public"
    token = spotipy.util.prompt_for_user_token(
        username=username, 
        scope="playlist-modify-public user-top-read",
        client_id="783950f05f6243ae87c1b916604ed1f9",
        client_secret="9ada72d264a444d38bd1617224c4f726",
        redirect_uri="https://example.com/callback"
    )
    return token

r = praw.Reddit(client_id = "dCMP8RkPkfM6-w",
                client_secret = "2lw2jSKMhoUtoLqaqOxiPeJKKjlrXg",
                username = "mzig2222",
                password = "Ziggysmalls22",
                user_agent = "freshMixv1")

username='mzig22222'
s = spotipy.Spotify(sp_Authenticate(username))

a = s.album('https://open.spotify.com/album/4GNIhgEGXzWGAefgN5qjdU')

for track in a['tracks']['items']:
    print(track['id'])