import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests
import os




SPOTIPY_CLIENT_ID = "6a1ab571e45c496a945ed49adaa48e0f"
SPOTIPY_CLIENT_SECRET = "08232eedea324eb6bda2967cba7482d3"
SPOTIPY_REDIRECT_URI = "http://example.com"
OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'
BILLBOARD_URL = "https://www.officialcharts.com/charts/singles-chart/"
# auth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
#                             redirect_uri=SPOTIPY_REDIRECT_URI, scope="playlist-modify-private", state=None,
#                             cache_path="token.txt", username=None, proxies=None,
#                             show_dialog=True, requests_session=True,
#                             requests_timeout=None)

# auth.get_access_token(code=None, as_dict=True, check_cache=True)



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"))

userid = sp.current_user()["id"]

date = input("Which year would you like to travel to? Type the date in this format YYYYMMDD: ")

response = requests.get(f"{BILLBOARD_URL}{date}")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

# print(web_page)

titles = soup.find_all(name="div", class_="title")

title_list = [str.strip(title.getText()) for title in titles]

print(title_list)
playlist_date = f" {date[0]}{date[1]}{date[2]}{date[3]}-{date[4]}{date[5]}-{date[6]}{date[7]}"
year = playlist_date.split("-")[0]
# create song URI list from Spotify
uri_of_titles = []
for track in title_list:
        query = sp.search(q=f"track:{track} year:{year}", type="track", limit=1)
        try:
                uri_of_titles.append(query["tracks"]["items"][0]["uri"])
        except IndexError:
                print(f"{track} doesn't exist in Spotify. Skipped.")


#create playlist

playlist = sp.user_playlist_create(userid, public=False, name=f"{playlist_date} UK Top 100 Singles",description= "Udemy 100 days of code day 46")

sp.playlist_add_items(playlist["id"], uri_of_titles, position=None)









