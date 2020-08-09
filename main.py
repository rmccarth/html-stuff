import requests
from bs4 import BeautifulSoup as bs4

main_page = "https://www.youtube.com/feed/trending"

response = requests.get(main_page)
soup = bs4(response.text, features='lxml')
links = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})

print(links)

