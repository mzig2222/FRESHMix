import praw
import spotipy
import spotipy.util
from spotipy.oauth2 import SpotifyOAuth
import datetime as dt

def sp_Authenticate(username):
    scope = "playlist-modify-public"
    token = spotipy.util.prompt_for_user_token(
        username=username, 
        scope="playlist-modify-public user-top-read",
        client_id="**********",
        client_secret="************",
        redirect_uri="https://example.com/callback"
    )
    return token

r = praw.Reddit(client_id = "******************",
                client_secret = "*****************",
                username = "*******", ##replace with your Reddit username & pass
                password = "********",
                user_agent = "freshMixv1")

subs = ["HipHopHeads", "Popheads", "Indieheads"]

username='*******' #replace with Spotify username
s = spotipy.Spotify(sp_Authenticate(username))

id = s.me()['id']

today = dt.date.today()
week_ago = today - dt.timedelta(days=7)

pl = s.user_playlist_create(id, "FRESHMix Playlist " + week_ago.strftime("%m/%d/%Y") + " - " + today.strftime("%m/%d/%Y"), public=True, collaborative=False, description="")
pl_id = pl['id']

tracks = []
urls = []
hashed_urls = {}

for name in subs:
    sub = r.subreddit(name).top('week')
    for post in sub:
        if "[FRESH]" in post.title or "[FRESH EP]" in post.title or "[FRESH ALBUM]" in post.title:
            
            # skipping duplicates
            if post.url in hashed_urls:
                continue
            else:
                hashed_urls[post.url] = ''
            
            #print(post.title.split(']')[1] + ' // ' + post.url)
            tracks.append(post.title.split(']')[1])

            if "https://open.spotify.com/track" in post.url: # spotify links - tracks
                print("adding track: " + post.title + " at " + post.url)
                urls.append(post.url)

            elif "https://open.spotify.com/album" in post.url: #spotify links - albums 
                print("adding album: " + post.title + " at " + post.url)
                a = s.album(post.url)
                for track in a['tracks']['items']:
                    urls.append('https://open.spotify.com/track/' + track['id'])
                    if len(urls) == 99:
                        s.user_playlist_add_tracks(id, pl_id, urls, position=0)
                        urls = []
            

            #buffering
            if len(urls) == 99:
                s.user_playlist_add_tracks(id, pl_id, urls, position=0)
                urls = []


#print(tracks)
s.user_playlist_add_tracks(id, pl_id, urls, position=0)

