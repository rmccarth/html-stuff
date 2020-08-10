import requests
from bs4 import BeautifulSoup as bs4
import json
import re

main_page = "https://www.youtube.com/feed/trending"

response = requests.get(main_page)
soup = bs4(response.text, 'html.parser')
scripts = soup.find_all('script')

for script in scripts:
    
    urls = re.findall(r"/watch(.*?)[\"]", str(script))
    if len(urls) > 1:
        for url in urls:
            url = url.split("\\n")[0]
            url = "https://www.youtube.com/watch" + url
            print(url)


