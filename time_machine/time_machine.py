import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv

load_dotenv()

# 2005-07-16

# 1. Web scrapping from Billboard:

URL = "https://www.billboard.com/charts/hot-100/"

year = input(
    "What year would you like to travel to? Type the date in this format YYYY-MM-DD: ")


response = requests.get(f"{URL}/{year}")
top_billboard = response.text

soup = BeautifulSoup(top_billboard, "html.parser")

song_list = []
all_songs = soup.find_all(
    name="ul", class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max")


for song in all_songs:
    song_list.append(song.li.h3.getText().strip())


# 2. Creating a playlist in Spotify

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI')

scope = "playlist-modify-public"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                     client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope))

user_id = sp.current_user()['id']

playlist = sp.user_playlist_create(
    user_id, name='Ayo', public=True, description='List of 100 billboard songs from the past')
playlist_id = playlist['id']


# 3. Searching and adding "all_songs" into my spotify playlist

# track_set = set()
for i, name in enumerate(song_list):
    result = sp.search(q=name, type='track')
    uri_link = result['tracks']['items'][0]['uri']
    sp.playlist_add_items(playlist_id, items=[uri_link])
    # track_set.add(uri)
    print(f"{i}.{name}: {uri_link}")
