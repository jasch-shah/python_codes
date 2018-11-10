import bs4
import lxml #xml parser
from bs4 import BeautifulSoup as soup
from urllib2 import urlopen

def news(xml_news_url):
	
	Client=urlopen(xml_news_url)
	xml_page=Client.read()
	Client.close()
	
	soup_page=soup(xml_page,"xml")
	
	news_list=soup_page.findAll("item")
	
	for news in news_list:
		print("\n")
		print(news.title.text)
		print(news.link.text)
		print(news.pubDate.text)	
		print("\n")



#you can add google news 'xml' URL here for any country/category 
news_url="https://news.google.com/news/rss/?ned=us&gl=US&hl=en"
sports_url="https://news.google.com/news/rss/headlines/section/topic/SPORTS.en_in/Sports?ned=in&hl=en-IN&gl=IN"

#now call news function with any of these url or BOTH

news(news_url)	
news(sports_url)