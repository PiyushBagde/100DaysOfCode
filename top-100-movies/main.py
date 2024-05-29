import requests
from bs4 import BeautifulSoup

response = requests.get(
    {your-url-goes-here-enclosed-in-quotes})
movies_html = response.text

soup = BeautifulSoup(movies_html, 'html.parser')

# the following i used for the specific website
all_movies = soup.find_all(name='h3', class_="title")

print(all_movies)
movie_title = [item.get_text() for item in all_movies]

movies = movie_title[::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
