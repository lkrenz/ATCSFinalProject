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
# Fetch the current user's data
# userid = input("Enter your user id: ")
playlists = spotify.user_playlists('liamkrenz')
name = input("Enter playlist name: ")
playlist_id = 0
for i in playlists["items"] : 
    if i["name"] == name :
        playlist_id = i["id"]
print(spotify.playlist(playlist_id))


