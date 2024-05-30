import os

import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

Client_ID = os.environ.get('Client_ID')
Client_secret = os.environ.get('Client_secret')

search_date = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD: ")

# make a get request to html
billboard_response = requests.get(f"https://www.billboard.com/charts/hot-100/{search_date}")
bill_board_html = billboard_response.text

soup = BeautifulSoup(bill_board_html, "html.parser")
print('parsed html')

all_songs = soup.find_all(name='h3', id="title-of-a-story")
print('found all song')

# create a list of top songs extracted from website
top_songs = [song.get_text().strip() for song in all_songs]
songs_list = top_songs[5:-16:4]
print("created song list")

# authenticate with spotify
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Client_ID, client_secret=Client_secret, scope=scope))
print('done spotify auth')

# get song track for all top 100 songs

songs_uri = []
for song in songs_list:
    result = sp.search(song, limit=1, type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        print(f'found {song}')
        songs_uri.append(uri)
    except:
        print(f"{song} is skipped, cuz it doesn't exits")

print('created songs uri')

# get current user id, it is not same as the display name
userid = sp.current_user()['id']
# print('create user id:' , userid)

# create a fresh private/public playlist for current user
playlist = sp.user_playlist_create(public=False,
                                   description=f"playlist created on {search_date}. These are the top 100 songs acc to bill board",
                                   name=f"{search_date} trending songs", user=userid)

# store the playlist id for newly created playlist
playlist_id = playlist['id']
print('created playlist id')
# print(playlist['id'])

# add songs to created playlist which accepts playlist_id just saved and list of songs Tracks
sp.playlist_add_items(playlist_id, songs_uri)
print('added song')
