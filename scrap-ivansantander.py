from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://ivansantander.com/index/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup)