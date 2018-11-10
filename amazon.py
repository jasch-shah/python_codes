import requests, bs4, webbrowser, sys

res = requests.get(productUrl, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
})
res.raise_for_status()

# Retrieve top search results links
soup = bs4.BeautifulSoup(res.txt, "html.parser")

# Open new tab for each results