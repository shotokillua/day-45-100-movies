import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
# print(soup.text)

movie_titles = soup.find_all(name="h3", class_="title")
# print(movie_titles)

title_text_list = [movie.getText() for movie in movie_titles]
# print(title_text_list)

# To print something in reverse >>> slice operator syntax [start: stop: step] beginning : end : stepsize of -1
reversed_list = title_text_list[::-1]
print(reversed_list)

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in reversed_list:
        file.write(f"{movie}\n")

