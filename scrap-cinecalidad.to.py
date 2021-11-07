from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.cine-calidad.com/latino/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

movies = soup.find_all('div', class_='postItem')

print(movies)

