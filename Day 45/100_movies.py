import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.timeout.com/film/best-movies-of-all-time")

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

all_movies = soup.find_all(name="h3", class_="_h3_cuogz_1")


movie_titles = [movie.getText() for movie in all_movies]

#print(movie_titles)

#add each movie to a file in reverse order

# with open ("movie_list.txt", "w") as f:
#     for n in range(len(movie_titles) -2, -1,  -1):
#         f.write(f"{movie_titles[n]}\n")
#         print(movie_titles[n])

## or splice to create list (1st h3 is not a movie -- ['Check out the best movies of all time as chosen by actors')
print(movie_titles[0:-1])

