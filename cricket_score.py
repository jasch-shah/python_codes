import bs4
from bs4 import BeautifulSoup as soup
from urllib2 import urlopen as uReq

my_url = "http://www.cricbuzz.com/"
Client = uReq(my_url)


html_page = Client.read()
Client.close()

soup_page = soup(html_page, "html.parser")

score_box = soup_page.findAll("div", {"class":"cb-col cb-col-25 cb-mtch-blk"})
score_box_len = len(score_box)
print(score_box_len)
for i in range(score_box_len):
	   print(score_box[i].a["title"])
	   print(score_box[i].a.text)
	   print()
