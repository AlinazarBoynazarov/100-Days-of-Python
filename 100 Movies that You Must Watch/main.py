import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
top_100_movies = response.text
soup = BeautifulSoup(top_100_movies, "html.parser")

movies = soup.find_all(name="h3", class_="title")

with open("movies_to_watch.txt", mode="w") as file:
    for movie_title in reversed(movies):
        movie = movie_title.getText()
        file.write(f"{movie}\n")
