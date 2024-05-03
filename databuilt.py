import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Define your credentials and redirection URI
SPOTIPY_CLIENT_ID = 'dda606479dd244a9b0948c01f155ac7a'
SPOTIPY_CLIENT_SECRET = 'd714739739a04b0fa662e521e1a85ff8'
SPOTIPY_REDIRECT_URI = 'http://localhost:3000'

# Define the required scope
# scope = "user-library-read"  # Adjust the scope according to the data you need access to

# Create the Spotify client

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    # scope=scope
))

playlists = spotify.user_playlists('liamkrenz')

# https://stackoverflow.com/questions/39086287/spotipy-how-to-read-more-than-100-tracks-from-a-playlist
def get_playlist_tracks(playlist_id):
    results = spotify.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results['items'])
    return tracks

name = input("enter playlist name: ")
playlist_id = ""
for i in playlists:
    if i["name"] == "dataset" : 
        playlist_id = i["id"]

playlist_data = get_playlist_tracks(playlist_id)

playlist = []
names = []

for i in playlist_data : 
    names.append(i["track"]["name"])
    playlist.append(spotify.audio_features(i["track"]["id"])[0])


