import os
import webbrowser

import requests
from bs4 import BeautifulSoup

query = raw_input('Enter song')
query = query.replace(' ', '+')

url = 'https://www.youtube.com/results?search_query=' + query
source_code = requests.get(url,timeout=15)
plain_text = source_code.text 
soup = BeautifulSoup(plain_text, "html.parser")

songs = soup.findAll('div', {'class': 'yt-lockup-video'})
song = songs[0].contents[0].contents[0].contents[0]
link = song['href']
webbrowser.open('https://www.youtube.com' + link)

