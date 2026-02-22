import spotipy
from spotipy.oauth2 import SpotifyOAuth

print("กำลัง login...")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="0c69180564c140c7ae80f992442f6393",
        client_secret="d52ad7ea15e34823a4e3fbc925c207a4",
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="playlist-read-private user-read-email playlist-read-collaborative",
        show_dialog=True
    )
)

playlists = sp.current_user_playlists()

me = sp.current_user()
print("Display Name:", me["display_name"])
print("Email:", me["email"])