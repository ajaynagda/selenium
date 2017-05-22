from urllib import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
	global pages
	try:
	
		html = urlopen(pageUrl)
		bsObj = BeautifulSoup(html,"lxml")

		for link in bsObj.find_all('a', href=True):
				if 'href' in link.attrs:
					if link.attrs['href'] not in pages:
						print link['href']
						newPage = link.attrs['href']
						print("----------------\n"+newPage)
						pages.add(newPage)
						getLinks(newPage)
	except IOError:
		print("This page is missing something! No worries though!")
	except ValueError:
		print("ValueError This page is missing something! No worries though!")
	
getLinks("http://www.example.com")